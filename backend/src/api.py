from typing import List

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from db_utils import get_existing_urls
from rag_utils import add_new_knowledge, run_rag_pipeline

# Setup FastAPI app
app = FastAPI()
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
    url: str | List[str]
    query: str


class Knowledge(BaseModel):
    url: str | List[str]


@app.post("/rag_query")
async def rag_query(rag_request: RAGQuery):
    """
    Retrieve relevant information from the DB and use it as context to generate
    an answer from an LLM.
    """
    result = run_rag_pipeline(rag_request.url, rag_request.query)
    return {"result": result}


@app.post("/add_knowledge")
async def add_knowledge(knowledge: Knowledge):
    """
    Add a new website to the DB.
    """
    add_new_knowledge(knowledge.url)
    return {"message": "success"}


@app.get("/get_knowledge_list")
async def get_knowledge_list():
    """
    Retrieve a list of URLs which are currently being stored in the DB.
    """
    urls = get_existing_urls()
    return {"urls": urls}
