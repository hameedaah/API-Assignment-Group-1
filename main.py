from fastapi import FastAPI
import random

app = FastAPI()

books = [
    {"title": "Book 1", "author": "Author 1"},
    {"title": "Book 2", "author": "Author 2"},
    {"title": "Book 3", "author": "Author 3"},
    {"title": "Book 4", "author": "Author 4"},
    {"title": "Book 5", "author": "Author 5"},
    {"title": "Book 6", "author": "Author 6"},
    {"title": "Book 7", "author": "Author 7"},
    {"title": "Book 8", "author": "Author 8"},
    {"title": "Book 9", "author": "Author 9"},
    {"title": "Book 10", "author": "Author 10"},
    {"title": "Things fall apart", "author": "Chinua Achebe"},
    {"title": "Independence", "author": "Hope Agbaje"},
    {"title": "Last days in forcados", "author": "Bola Tinubu"},
    {"title": "48 laws of power days", "author": ""},
]


#ALL FUNCTIONS
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def get_all_books():
    return books

def get_book_by_title(book_title):
    new_books = []
    for book in books:
        if book_title.lower() == book["title"].lower():
            new_books.append(book)
    return new_books

def get_book_by_author(author_name):
    new_books = []
    for book in books:
        if author_name.lower() == book["author"].lower():
            new_books.append(book)
    return new_books


def add_new_book_to_list(title: str, author: str):
    for existing_book in books:
        if existing_book["title"].lower() == title.lower() and existing_book["author"].lower() == author.lower():
            return "Error: This book already exists."

    books.append({"title": title, "author": author})
    return f"Success: {title} has been added"

def update_book_by_title(current_title: str, new_title: str = None, new_author: str = None):
    for book in books:
        if book["title"].lower() == current_title.lower():
            if new_title:
                book["title"] = new_title
            if new_author:
                book["author"] = new_author
            return {"message": "Book updated successfully"}
    return {"error": "Book not found"}

def get_book_by_prime():
    new_books = []
    for book in books:
        # split_val = book["title"][-1]
        split_title = book["title"].split()
        if len(split_title) >= 2 and split_title[1].isdigit():
            split_val = int(split_title[1])
            if is_prime(split_val):
                new_books.append(book)
    return new_books

def delete_book_by_title(book_title):
    for book in books:
        if book_title.lower() == book["title"].lower():
            books.remove(book)
    return f"Success: {book['title']} has been removed"

def find_empty_authors(book_title):
    for book in books:
        if book_title.lower() == book["title"].lower() and book["author"] == "":
            return f"{book['title']} has an empty author"
    return "This book has an author"

def search_by_keyword(the_keyword):
    search_results = []
    for book in books:
        if the_keyword.lower() in book["title"].lower() or (book["author"] == "" and the_keyword.lower() in book["title"].lower()):
            search_results.append({"title": book["title"], "author": book["author"]})
    if search_results:
        return search_results
    else:
        return "No matches in the database"



#ALL ENDPOINTS
@app.get("/")
def read_root():
    return {"Python is the best programming language!"}

#Return all books
@app.get("/all-books")
def all_books():
    response = get_all_books()
    return response

#Return books by title
@app.post("/get-book-by-name")
def book_by_name(request:dict):
    book_name = request["book_name"]
    response = get_book_by_title(book_name)
    return response

#Return books by author
@app.post("/get-book-by-author")
def book_by_author(request: dict):
    author = request["author"]
    response = get_book_by_author(author)
    return response

#Return books with prime numbers as their suffix"
@app.get("/all-books-with-prime")
def book_by_prime():
    response = get_book_by_prime()
    return response

#Add a new book to the list
@app.post("/add-new-book")
def add_book(request: dict):
    title = request["title"]
    author = request["author"]
    result = add_new_book_to_list(title, author)

    if result.startswith("Error"):
        return {"error": result}
    return {"message": result}

#Remove a book from the list
@app.delete("/delete-book-by-title")
def del_book(request:dict):
    book_name = request["book_name"]
    response = delete_book_by_title(book_name)
    return response

#Return a random book
@app.get("/random-book")
def random_book():
    return random.choice(books)

#Count and return the number of books in our lst
@app.get("/count-books")
def count_books():
    return {"count": len(books)}

#Update the title and author of a book
@app.put("/update-book")
def update_book(current_title: str, new_title: str = None, new_author: str = None):
    result = update_book_by_title(current_title, new_title, new_author)
    return result

#Check if book has an author
@app.post("/return-empty-authors-by-title")
def find_book(request:dict):
    book_name = request["book_name"]
    response = find_empty_authors(book_name)
    return response

#Find books and authors by keywords
@app.get("/search-books-by-keywords")
def search_book(the_keyword: str):
    result = search_by_keyword(the_keyword)
    return result