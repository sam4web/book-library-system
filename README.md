# Book Library System Project

## Overview:

Book Library System is a command-line application designed to manage a collection of books in a library. It allows users to perform various operations related to book management, such as adding new books, viewing existing books, searching for books, borrowing and returning books, and more.

## Features:

- **User Authentication**: Users can create an account with a unique username and password to access the library system securely.
- **Add Books**: Easily add new books to the library by providing title, author, genre, and publication year information.
- **View Books**: View all books in the library along with their details such as title, author, and genre.
- **Search Books**: Search for books by title, author, or genre to quickly find the desired book.

## Prerequisites:

- Python 3 installed on your system.
- SQLite installed (usually comes pre-installed with Python).

## Installation:

1. Clone the repository:

```bash
git clone <repository-url>
```

2. Navigate to the project directory:

```bash
cd book_library_system
```

3. (Optional) Set up a virtual environment:

```bash
python3 -m venv venv
source venv/Scripts/activate
```

4. Install dependencies:

```bash
pip install -r src/requirements.txt
```

## Usage:

1. Run the application:

```bash
python src/main.py
```

2. Follow the on-screen instructions to interact with the Book Library System. You can add books, view books, search for books, etc.

### Notes:

- Modify the src/main.py file or add more functionality as needed for your specific requirements.

- Make sure you have SQLite installed on your system for the database functionality to work properly.

## Deactivation (Optional):

1. If you used a virtual environment, deactivate it once you're done:

```bash
deactivate # Deactivate virtual environment
```

## Contributions

Contributions are welcome! If you have ideas for improvements or new features, feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
