# ParagonAI Backend - WIP

## Getting Started

### Prerequisites
Make sure you have the following installed:
- Python 3.9+
- Pip (package installer for Python)
  
### Installation

1. Clone the repository

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Running the App

1. Create .env file and add the following values (field values are examples):
    ```bash
    DB_DIR_NAME="chroma_db"
    DB_COLLECTION_NAME="langchain"
    OPENAI_API_KEY= #optional - you can use set_openai_api_key/ endpoint to set it or this env veriable
    ```

2. Run the development server using Uvicorn:
    ```bash
    fastapi dev src/api.py
    ```

3. The app will be available at `http://127.0.0.1:8000`.

### Testing the API

To explore and test the API, you can use the automatically generated OpenAPI docs provided by FastAPI:
- OpenAPI docs: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`
