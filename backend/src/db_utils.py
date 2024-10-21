import os
from typing import List

from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_core.documents.base import Document
from langchain_core.embeddings.embeddings import Embeddings

load_dotenv()
DB_DIR_NAME = os.getenv("DB_DIR_NAME")
DB_COLLECTION_NAME = os.getenv("DB_COLLECTION_NAME")


def _get_persistent_directory():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    persistent_directory = os.path.join(current_dir, "db", DB_DIR_NAME)
    return persistent_directory


def _get_db_object(persistent_directory: str, embedder: Embeddings = None):
    return Chroma(
        collection_name=DB_COLLECTION_NAME,
        embedding_function=embedder,
        persist_directory=persistent_directory,
    )


def get_existing_urls():
    persistent_directory = _get_persistent_directory()
    if not os.path.exists(persistent_directory):
        print("DB is empty. Please add entries.")
        return []
    else:
        db = _get_db_object(persistent_directory)
        metadata = db.get(include=["metadatas"]).get("metadatas")
        urls = list(set([doc.get("source") for doc in metadata]))
        return urls


def add_to_db(embedder: Embeddings, docs: List[Document]):
    persistent_directory = _get_persistent_directory()
    if not os.path.exists(persistent_directory):
        print(f"Creating vector store in {persistent_directory}")
        db = Chroma.from_documents(
            docs, embedder, persist_directory=persistent_directory
        )
        print(f"Finished creating vector store in {persistent_directory}")
    else:
        print(
            f"Vector store {persistent_directory} already exists. Adding to existing store."
        )
        db = _get_db_object(persistent_directory, embedder)
        db.add_documents(documents=docs)


def remove_from_db(url: str):
    persistent_directory = _get_persistent_directory()
    if not os.path.exists(persistent_directory):
        print("DB does not exist. Cannot delete entries.")
    else:
        db = _get_db_object(persistent_directory)
        ids = db.get(where={"source": f"{url}"}, include=[]).get("ids")
        if ids:
            db.delete(ids)
            print(f"Successfully deleted entries from {url}.")
        else:
            print(f"No entries found for {url} .")


def retrieve_docs(
    url: str,
    embedder: Embeddings,
    query: str,
    search_type: str = "similarity",
    search_kwargs: int = 3,
):
    persistent_directory = _get_persistent_directory()
    if not os.path.exists(persistent_directory):
        print("Error: DB directory does not exist. Please add data before querying.")
        return
    else:
        db = _get_db_object(persistent_directory, embedder)
        retriever = db.as_retriever(
            search_type=search_type,
            search_kwargs={"k": search_kwargs, "filter": {"source": url}},
        )
        relevant_docs = retriever.invoke(query)
        return relevant_docs
