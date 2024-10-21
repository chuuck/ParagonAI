from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader


def format_documents(): ...


def scrape_to_documents(url: str, chunk_size: int = 500, chunk_overlap: int = 50):
    print(f"Scraping data from {url}")
    loader = WebBaseLoader(url)
    document = loader.load()

    print("Splitting data into chunks")
    text_splitter = CharacterTextSplitter(
        separator="\n", chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )
    document_chunks = text_splitter.split_documents(document)
    print(f"Created {len(document_chunks)} chunks.")

    return document_chunks
