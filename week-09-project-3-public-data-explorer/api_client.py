import requests


open_library_api = "https://openlibrary.org/search.json"

def search_book(user_search):
    parameters = {
        "title": user_search,
        "limit": 1,
        "fields": "title, author_name, first_publish_year"
    }

    # 1. CATCH NETWORK ERRORS
    try:
        response = requests.get(open_library_api, params=parameters)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return f"Network Error: Could not connect to API {(e)}"

    # 2. PARSE THE DATA SAFELY
    data = response.json()

    # Use .get() to safely check for the 'docs' list
    books = data.get('docs', [])
    if not books:
        return "No books found"
        
    # Extract the first book
    book = books[0]
    book_name = book.get('title', 'Unknown Title')

    # 3. CATCH DATA PARSING ERRORS (IndexError / KeyError)
    try:
        author_name = book['author_name'][0]
    except (IndexError, KeyError):
        author_name = "Unknown Author"

    try:
        publish_year = book['first_publish_year']
    except KeyError:
        publish_year = "Unknown Year"

    return f"Book title: {book_name}\nAuthor's name: {author_name}\nFirst Publish year: {publish_year}"