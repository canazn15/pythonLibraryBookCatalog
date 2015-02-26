__author__ = 'carlo'
import sys, os
from mongoengine import *
from catalogue import *
from libcase import *

mainCount = 0

def main(argv):
    # Default database args:
    database = "pythonDB"
    # user = "root"
    # password = "mongodb"
    # host = "localhost"
    # port = 27017
    # authTable = "admin"
    # alias = 'carlo'
    #db = connect(database, username='root', password='mongodb', host="localhost", port=28017, alias="admin")
    db = connect(database)

    def retry(input):
        #try:
        if input == "y":
            #command = int(gui())
            #menu(db,database,command)
            main(argv)
        elif input == "n":
            print "\n\nGoodbye!"
            #sys.exit()
        else:
            print "Invalid Entry."
            input = raw_input("Load Menu Options?(y/n) ")
            input = input.lower()
            retry(input)
        #except:
        sys.stdin = sys.__stdin__
        # command = int(gui())
        # menu(db,database,command)

    # Show GUI and grab the user's menu command
    command = int(gui())
    # Run the menu command helper
    menu(db,database,command)
    # Ask if the user wants to load the menu
    retry(raw_input("\nLoad Menu Options?(y/n) "))


# Create a basic menu GUI for the catalogue
def gui():

    gui ="\n"
    gui+= "-------------------Enter a command:-------------------\n"
    gui+= "1. Initialize the database.\n"
    gui+= "2. Create book and Add it to one or more libraries.\n"
    gui+= "3. Search for a book based on a category or categories. \n"
    gui+= "4. Add non-referenced book to library. \n"
    gui+= "5. Run Unit Tests\n"
    gui+= "6. Exit program.\n "
    gui+= "------------------------------------------------------"
    print gui
    input = raw_input("User Command: ")
    while input not in ['1','2','3','4','5','6']:
        print "Invalid Command! Try Again."
        input = raw_input("User Command: ")
    return input

def menu(db, database, command):
    # Initialize pre-configured data model menu item
    if(command == 1):
        # Drop existing database
        db.drop_database(database)

        # Initialize a catalogue object
        initCatalogue = catalogue()

        # Get pre-defined libraries
        libs = initLibraries(database)
        print "------Library------"
        for lib in libs:
            # create each library to database
            initCatalogue.createLibrary(database, lib)
            print "Created: "+lib.name

        # Get pre-defined books
        books = initBooks(database)
        print "------Books------"
        for book in books:
            # create each book to database
            initCatalogue.createBook(database, book)
            print "Created: "+book.title
        print "\n"
        # Add all books to Toronto Reference Library
        for book in Book.objects:
             initCatalogue.addBookToLibrary(database, book.title, "Toronto Reference Library")

        # Add these 3 books to Robarts Library
        for book in Book.objects(title="Harry Potter and the Half-Blood Prince"):
            initCatalogue.addBookToLibrary(database, book.title, "Robarts Library")
        for book in Book.objects(title="The Diary of a Young Girl"):
            initCatalogue.addBookToLibrary(database, book.title, "Robarts Library")
        for book in Book.objects(title="The French Market Cookbook"):
            initCatalogue.addBookToLibrary(database, book.title, "Robarts Library")

        # Add ne Fiction books to Library
        for book in Book.objects(category__ne="Fiction"):
            initCatalogue.addBookToLibrary(database, book.title, "Spadina Road Library")

    # Create a book menu item
    elif(command == 2):
        # Create a catalogue object called catalog
        catalog = catalogue()
        # Grab attributes of the new book from user.
        title = raw_input("Title: ")
        author = raw_input("Author: ")
        publisher = raw_input("Publisher: ")
        categories = raw_input("Category (separate w/ space): ")
        category = map(str, categories.split())
        # Create book object based on attributes
        book = newBook(title, author, publisher, category)
        # Use helper class to save the book object to database
        catalog.createBook(database, book)

        # Add a book to the library
        input = ""
        while(input!="y" and input!="n"):
            input = raw_input("Add this book a library?(y/n) ").lower()
            # If user say yes about adding book to library
            if(input=="y"):
                print "\nPlease specify which libraries you want to add this book."
                libs = raw_input("Library Name: ")
                print "\n"
                libs = libs.split(";")
                for lib in libs:
                    catalog.addBookToLibrary(database, book.title, lib)
            # If user say no about adding book to library
            elif(input=="n"):
                print "\nThis %(title)s was created but not added to a library."%{'title':title}
            # Invalid entry and try again
            else:
                print "Invalid entry! Please retry again."

    # Search for a book menu item
    elif(command == 3):
        # Create a catalogue object called catalog
        catalog = catalogue()
        print "Search the location of a book based one or more categories."
        print "Note: split multiple categories using ';' as delimiter."
        print "------------------------------------------------------"
        categories = raw_input("Category: ")
        category = map(str.strip, categories.split(";"))
        print category
        catalog.searchBookCategory(database,category)

    # Add book to a library
    elif(command == 4):
        bookTitle = raw_input("Book Title: ")
        book = Book.objects(title=bookTitle)
        if not book:
            print "This book does not exist."
        else:
            # Check if book object already is in a library
            if Library.objects(book__in=book):
                print "Attention: This book is already in a library. "
            # Else add book object to library
            else:
                catalog = catalogue()
                libName = raw_input("Library Name: ")
                # Create a catalogue object called catalog
                libs = libName.split(";")
                for lib in libs:
                    catalog.addBookToLibrary(database, bookTitle, lib)

    # Run UnitTests
    elif(command == 5):
        # Ask for testcase number
        num = int(raw_input("Testcase Number: "))
        # Testcase number has to be number
        while num not in [1,2,3,4]:
        #while num < 1 or num > 4:
            print "Invalid Entry. Select a Testcase Number from 1 to 4."
            num = int(raw_input("Testcase Number: "))
        # create testcase object called test
        test = testcase(db,database,num)
        # run the testcase
        test.runTestcase(num)

    # Exit program menu item
    elif(command == 6):
        print "Goodbye!"
        sys.exit()

    # Invalid entry and try again
    else:
        print "\n\n\nInvalid entry! Please retry again:"

if __name__ == "__main__":
  main(sys.argv)