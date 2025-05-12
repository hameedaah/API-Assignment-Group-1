

#print(get_book_by_title("book 1"))

from fastapi import FastAPI, Request

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
]
app = FastAPI()

def get_all_books():
    return books

def get_book_by_title(book_title):
    new_books = []
    for book in books:
        if book_title.lower() == book["title"].lower():
            new_books.append(book)
    return new_books

def post_book_by_author(author_name):
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
    return "Success"

def delete_book_by_title(book_title):
    for book in books:
        if book_title.lower() == book["title"].lower():
            books.remove(book)
        return {"message": f"✅ Success: '{book_title}' has been removed."}
    return {"error": f"❌ Book '{book_title}' not found."}

def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
        
def update_book_by_title(current_title: str, new_title: str = None, new_author: str = None):
    for book in books:
        if book["title"].lower() == current_title.lower():
            if new_title:
                book["title"] = new_title
            if new_author:
                book["author"] = new_author
            return {"message": f"✅ Book '{current_title}' updated", "updated_book": book}
    return {"error": "❌ Book not found"}
#ALL ENDPOINTS

@app.get("/")
def read_root():
    return {"Python is the best programming language!"}


@app.get("/all-books")
def all_books():
    response = get_all_books()
    return response


@app.post("/get-book-by-name")
def book_by_name(request:dict):
    book_name = request["book_name"]
    response = get_book_by_title(book_name)
    return response

@app.post("/get-book-by-author")
def book_by_author(request: dict):
    author = request["author"]
    response = post_book_by_author(author)
    return response

# Route to add a new book
@app.post("/add-new-book")
def add_book(request: dict):
    title = request["title"]
    author = request["author"]
    result = add_new_book_to_list(title, author)

    if result.startswith("Error"):
        return {"error": result}
    return {"message": result}

# Route to delete a book by title
@app.delete("/delete-book")
def delete_book(request: dict):
    book_title = request["title"]
    result = delete_book_by_title(book_title)
    return f"book_title: {book_title} has been deleted"


# Route to Get books with prime number suffix
@app.get("/prime-books")
def get_prime_books():
    prime_books = []
    for book in books:
        title_parts = book["title"].split()
        if len(title_parts) == 2 and title_parts[1].isdigit():
            if is_prime(int(title_parts[1])):
                prime_books.append(book)
    return prime_books

#Route to update a book by title and author
@app.put("/update-book")
def update_book(current_title: str, new_title: str = None, new_author: str = None):
    result = update_book_by_title(current_title, new_title, new_author)
    return result

# Route to count the number of books
@app.get("/count-books")
def count_books():
    return {"count": len(books)}

# Route to pick a random book
@app.get("/random-book")
def random_book():
    import random
    if books:
        return random.choice(books)
    else:
        return {"error": "No books available"}