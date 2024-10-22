<p align="center">
  <img src="https://github.com/chuuck/ParagonAI/blob/feature/selecting_kb_sources/assets/Paragon_Banner.jpg" />
</p>

#
ParagonAI is an open-source project designed to make interacting with large bodies of information simple and efficient. By leveraging Retrieval-Augmented Generation (RAG), ParagonAI allows users to build a custom knowledge base by providing URLs, from which it extracts, stores, and indexes relevant content. Users can then ask natural language questions about the information, receiving precise, contextually relevant answers.

## 1. Getting Started :rocket:

### 1.1. Front-End

To install all packages and start the front-end app run these commands

```
cd frontend
npm install
npm run dev
```

### 1.2. Back-end

#### Prerequisites
Make sure you have the following installed:
- Python 3.9+
- Pip (package installer for Python)
  
#### Installation


1. Create a virtual environment and activate it:
    ```bash
    cd backend
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

#### Running the App

1. Create .env file and add the following values (field values are examples):
    ```bash
    EMBEDDING_MODEL='sentence-transformers/all-MiniLM-L6-v2'
    GENERATION_MODEL="microsoft/phi-1_5"
    DB_DIR_NAME="chroma_db"
    DB_COLLECTION_NAME="langchain"
    ```

2. Run the development server using Uvicorn:
    ```bash
    fastapi dev src/api.py
    ```

3. The app will be available at `http://127.0.0.1:8000`.

#### Testing the API

To explore and test the API, you can use the automatically generated OpenAPI docs provided by FastAPI:
- OpenAPI docs: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

