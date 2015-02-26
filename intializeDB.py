from library import *
from book import *

__author__ = 'carlo'


def initLibraries(database):

    # Initializing 3 library branches.
    lib = []
    lib.append(newLibrary("Toronto Reference Library",
                         "789 Yonge Street Toronto, ON M4W 2G8",
                         "Rob Ford"))

    lib.append(newLibrary("Robarts Library",
                         "130 St. George Street Toronto, ON M5S 1A5",
                         "Doug Yancy"))

    lib.append(newLibrary("Spadina Road Library",
                         "10 Spadina Road Toronto, ON M5R 2S7",
                         "Christian Higgins"))
    return lib


def initBooks(database):

    # Initializing 5 books.
    book = []
    book.append(newBook("Harry Potter and the Deathly Hallows",
                        "J.K. Rowling",
                        "Bloomsbury Publishing",
                        ["Fiction","Thriller","Fantasy"]))

    book.append(newBook("Harry Potter and the Half-Blood Prince",
                        "J.K. Rowling",
                        "Bloomsbury Publishing",
                        ["Fiction","Thriller","Fantasy"]))

    book.append(newBook("The Diary of a Young Girl",
                        "Anne Frank",
                        "Bantam Books",
                        ["Non-Fiction","Memoir"]))

    book.append(newBook("Around My French Table",
                        "Dorie Greenspan",
                        "Rux Martin Publishing",
                        ["Cooking","French"]))

    book.append(newBook("The French Market Cookbook",
                        "Clotilde Dusoulier",
                        "Clarkson Potter Publishing",
                        ["Cooking","French","Vegetarian"]))
    return book

