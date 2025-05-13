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
```
http://127.0.0.1:8000
```
## The API Endpoints
### GET /all-books  
Search for books by title.
Request body:  
```
{
  "book_name": "Book 1"
}
```
### POST /get-book-by-author
Search for books by author.
Request body:  
```
{
  "author": "Author 1"
}
```
### POST /add-new-book
Add a new book to the collection.
Request body:  
```
{
  "title": "New Book",
  "author": "New Author"
}
```

### DELETE /delete-book-by-title
Deletes a book by its title.
Request body:  
```
{
  "book_name": "Book 1"
}
```

### GET /random-book
Returns a random book from the list.

### GET /count-books
Returns the total number of books in the list.

### PUT /update-book
Update the title or author of a book.
Query Parameters:  
current_title (required)
new_title (optional)
new_author (optional)

### POST /return-empty-authors-by-title
Checks if a book has an empty author field.
Request body:  
```
{
  "book_name": "48 laws of power days"
}
```
### PUT /search-books-by-keywords
Searches books by keyword in the title or if the author is empty.
Query parameter:  
(the_keyword)

## Helper Functions
```
1. get_all_books()
2. get_book_by_title(title)
3. post_book_by_author(author)
4. add_new_book_to_list(title, author)
5. update_book_by_title(current_title, new_title, new_author)
6. delete_book_by_title(title)
7. find_empty_authors(title)
8. search_by_keyword(keyword)
```
## Summary
This project is a FastAPI-based Book API that manages a simple in-memory list of books. It supports common operations such as retrieving all books, searching by title or author, adding new entries, updating existing ones, and deleting by title. It also includes extra features like keyword search, detecting books with empty authors, and returning a random book. Designed as a lightweight and beginner-friendly API, it demonstrates how to build and structure endpoints using FastAPI. All functionalites are accessible by using SwaggerUI.
