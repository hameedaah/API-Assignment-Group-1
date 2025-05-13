# :books: Book Management API with FastAPI

This is a FastAPI application for managing a list of books. It includes endpoints for retrieving, adding, updating and deleting books based on various criteria like title, author, and patterns like titles ending with prime numbers. You can also fetch random books, check for missing authors, and use keywords to search for books.

---

## :rocket: Getting Started

### Requirements

- Python 3.8+
- FastAPI
- Uvicorn

### Installation

- Clone the repository:
 ```
   git clone <your-repo-url>
   cd <your-project-directory>
 ```

### Running the Application
1. If FASTAPI and uvicorn are not already installed, install them with:
   ```
   pip install fastapi uvicorn
   ```
3. Run the server:
    ```
    uvicorn main:app --reload
     ```
Replace main with the name of  your python file.

The app will start on:
http://127.0.0.1:8000

