#! /usr/local/bin/python3

from stats import get_num_words, count_chars, report_all
from os import path
import sys

# BOOKS = ["frankenstein.txt"]
BOOKPATH = "./books"


def check_args(arg_vals):
    arg_count = False
    book_name = None
    book_available = False
    if 1 < len(arg_vals) < 3:
        arg_count = True
        book_name = arg_vals[1]
        if path.isfile(book_name):
            book_available = True
    return arg_count, book_name, book_available


def get_book_name(arg_vals):
    return arg_vals[1]


def get_book_text(filepath):
    """
    get the text of a book
    filepath: string, the filepath to the book to examine
    """
    with open(filepath) as f:
        print(f"reading {filepath}")
        file_contents = f.read()
    return file_contents


def main():
    arg_count, book_name, book_available = check_args(sys.argv)
    if arg_count and book_name and book_available:
        # print("running main.py")
        # book_path = path.join(BOOKPATH, book)
        book_text = get_book_text(book_name)
        # print_book_text(book_text)
        num_words = get_num_words(book_text)
        # print(f"\n\n\n{num_words} words found in the document")
        char_count = count_chars(book_text)
        # print(char_count)
        report_all(book_name, num_words, char_count)
    else:
        if not arg_count:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)
        if not book_available:
            raise Exception(f"{book_name} is not currently available")
            sys.exit(1)
        print("This would be my usage statement")


if __name__ == "__main__":
    main()

