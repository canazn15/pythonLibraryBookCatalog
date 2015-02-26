__author__ = 'carlo'
from mongoengine import *
from library import *

class Book(Document):

    title = StringField(max_length=200, required=True)
    author = StringField(max_length=200)
    publisher = StringField(max_length=200)
    category = ListField(StringField(max_length=200))

class newBook:

    def display(self):
        print self.title
        print self.author
        print self.publisher
        print self.category

    def __init__(self, title, author, publisher, category):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.category = category