# Week 9 — Project 3: Public Data Explorer
## 📌 Project Overview
This is a Command-Line Interface (CLI) application built in Python that allows users to search for books using the Open Library API. It fetches real-time data, parses the JSON response, and displays the book title, author, and first publish year.

## 🛠️ Technologies Used
- Python 3

- Requests Library (for handling HTTP GET requests to the Open Library API)

- JSON (for parsing the API data)

## 🚀 How to Run
1. Clone the repository and navigate to this folder:

```bash
cd week-09-project-3-public-data-explorer
```
2. Create and activate a virtual environment (optional but recommended).

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```
4. Run the program:

```bash
python main.py
```
## 🧠 What I Learned & Challenges

- API Integration: I learned how to use the requests library to send parameters (like title, limit, and fields) to an external API.

- Handling JSON: I learned that API responses are nested dictionaries and lists. I had to navigate through data['docs'][0] to find the specific book details.

- Defensive Programming (Error Handling): I used try/except blocks to handle network failures (requests.exceptions.RequestException) and missing data (KeyError and IndexError). I realized that not every book in the Open Library has an author or a publish year, and my program needed to handle that gracefully instead of crashing.

- Separation of Concerns: I split my code into api_client.py (data fetching) and main.py (user interface) to keep the logic clean and organized.

## 🎥 Demo
- **Title:** Week 9 Project 3 Public Data Explorer Demo
- **Recording:** [https://www.loom.com/share/97b3ee8ebaa6452487067e2a02639719](https://www.loom.com/share/97b3ee8ebaa6452487067e2a02639719) 
- **Live URL:** N/A (script, not deployed)

## 📸 Sample Output
Welcome to FlexiSAF Library Book Search
1. Search for a Book 
2. Exit
Type either 1 or 2 to continue: 1
Enter the title of the book you want to search for: the hobbit
Book title: The Hobbit
Author's name: J.R.R. Tolkien
First Publish year: 1937
1. Search for a Book 
2. Exit
Type either 1 or 2 to continue: 1
Enter the title of the book you want to search for: xbtesh2w
This book title is not available. Would you like to try again?
1. Search for a Book 
2. Exit
Type either 1 or 2 to continue: 2
Thanks for using FlexiSAF Library Book Search!