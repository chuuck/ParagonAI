import os
from typing import List

from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

from db_utils import add_to_db, get_existing_urls, retrieve_docs
from scraper import scrape_to_documents

load_dotenv()
PROMPT_TEMPLATE = """
Answer the question based only on the following context:
{context}
- -
Answer the question based on the above context: {question}
"""


def add_new_knowledge(url: str, api_key: str = None):
    print("Adding new knowledge to DB.")
    if not api_key:
        api_key = os.getenv("OPENAI_API_KEY")

    existing_urls = get_existing_urls()
    if url in existing_urls:
        print(f"Documents from {url} already exist.")
    else:
        # Scrape and save to DB
        embedder = OpenAIEmbeddings(openai_api_key=api_key)
        docs = scrape_to_documents(url)
        add_to_db(embedder, docs)


def run_rag_pipeline(urls: List[str], query: str, api_key: str = None):
    print("Running RAG pipeline.")
    if not api_key:
        api_key = os.getenv("OPENAI_API_KEY")

    # Create embeddings for the document chunks
    embedder = OpenAIEmbeddings(openai_api_key=api_key)

    # Query the vector store
    relevant_docs = retrieve_docs(urls, embedder, query)
    if len(relevant_docs) == 0:
        return "Unable to find matching results. Check knowledge base is not empty."

    # Combine context from relevant documents
    context_text = "\n\n - -\n\n".join([doc.page_content for doc in relevant_docs])

    # Create prompt by using prompt template
    prompt_template = PromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query)

    # Initialise model for generating the response
    model = ChatOpenAI(openai_api_key=api_key)

    # Generate response
    response_text = model.invoke(prompt).content

    # Get sources of the relevant documents
    sources = set([doc.metadata.get("source", None) for doc in relevant_docs])

    # Format and return response including generated text and sources
    formatted_response = f"{response_text}\nSource: {sources}"
    return formatted_response


if __name__ == "__main__":
    urls = [
        "https://en.wikipedia.org/wiki/Harry_Potter",
        "https://en.wikipedia.org/wiki/Gilmore_Girls",
    ]
    # add_new_knowledge(urls)
    query = "Compare Harry Potter and Gilmore Girls."
    response = run_rag_pipeline(urls, query)
    print(response)
