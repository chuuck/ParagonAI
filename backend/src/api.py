from typing import List

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from db_utils import get_existing_urls_and_titles, remove_from_db
from rag_utils import add_new_knowledge, run_rag_pipeline

# Setup FastAPI app
app = FastAPI()
api_key_store = {}
load_dotenv()


# Enable CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_credentials=False,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class RAGQuery(BaseModel):
    urls: List[str]
    query: str


class URLTitlePair(BaseModel):
    url: str
    title: str


class URLList(BaseModel):
    urls: List[str]


class OpenAIAPIKey(BaseModel):
    api_key: str


@app.post("/rag_query")
async def rag_query(rag_request: RAGQuery):
    """
    Retrieve relevant information from the DB and use it as context to generate
    an answer from an LLM.
    """
    api_key = api_key_store.get("OPENAI_API_KEY")
    result = run_rag_pipeline(rag_request.urls, rag_request.query, api_key)
    return {"result": result}


@app.post("/add_knowledge")
async def add_knowledge(knowledge: List[URLTitlePair]):
    """
    Add a new website to the DB.
    """
    api_key = api_key_store.get("OPENAI_API_KEY")

    for item in knowledge:
        url = item.url
        title = item.title
        print(f"Processing URL: {url} with title: {title}")
        add_new_knowledge(url, title, api_key)

    return {"message": "Knowledge has been successfully added."}


@app.post("/remove_knowledge")
async def remove_knowledge(knowledge: URLList):
    """
    Remove specific website documents from a DB.
    """
    remove_from_db(knowledge.urls)
    return {"message": "Knowledge has been successfully removed."}


@app.get("/get_knowledge_list")
async def get_knowledge_list():
    """
    Retrieve a list of URLs which are currently being stored in the DB.
    """
    url_title_set = get_existing_urls_and_titles()
    return {"knowledge_list": url_title_set}


@app.post("/set_openai_api_key")
async def set_openai_api_key(api_key_request: OpenAIAPIKey):
    """
    Set OPENAI_API_KEY variable that will be use to calculate embeddings and
    generate a response.
    """
    api_key_store["OPENAI_API_KEY"] = api_key_request.api_key
    return {"message": "API key has been successfully set"}
