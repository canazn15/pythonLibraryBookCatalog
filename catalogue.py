from library import *
from book import *
from intializeDB import *

class catalogue:

    # Create a new library
    def createLibrary(self, database, library):
        newLibrary = Library(name = library.name,
                             address = library.address,
                             manager = library.manager)
        newLibrary.save()

    # Create a new book
    def createBook(self, database, book):
        newBook = Book(title = book.title,
                       author = book.author,
                       publisher = book.publisher,
                       category = book.category)
        newBook.save()

    # Add book into a library
    def addBookToLibrary(self,database,bookTitle,libraryName):

        checkLib = Library.objects(name=libraryName)
        if not checkLib:
            print 'Attention: The library "%(library)s" is non-existent. '%{'library':libraryName}
            newLib = ""
            # Ask for library information
            while(newLib!="y" and newLib!="n"):
                newLib = raw_input("Create new library?(y/n) ").lower()
                if(newLib == "y"):
                    print "--------Library--------"
                    print "Name: "+libraryName
                    newLibAddress = raw_input("Address: ")
                    newLibManager = raw_input("Manager: ")
                    # Create library
                    self.createLibrary(database, newLibrary(libraryName,newLibAddress,newLibManager))
                elif(newLib == "n"):
                    print "This book: \"%(title)s\" was created but not added to a library."%{'title':bookTitle}
                else:
                    print "Invalid entry! Please retry again."

        # Traverse through each library
        for library in Library.objects(name=libraryName):
            # Add that book into the library
            for book in Book.objects(title=bookTitle):
                library.update(push__book=book)
                out = """The book: "%(book)s" is now added to %(library)s.""" \
                         %{"book" : book.title,
                           "library" : library.name}
                print out

    # Search book from all library
    def searchBookCategory(self, database, category):

        print "\nResults:"
        print "--------"
        # Check for all books that have hit entered categories
        for book in Book.objects(category__all=category):
            # for each library check if book exist in it
            for library in Library.objects(book=book):
                out = """There is a %(category)s book titled: "%(book)s" located at "%(library)s." """ \
                        %{"category" : " + ".join(category),
                          "book" : book.title,
                          "library" : library.name}
                print out

        # If no book was found in the library
        if not Book.objects(category__all=category):
            print "No book was found based this category: "+" + ".join(category)

    def __init__(self):
        print ""
