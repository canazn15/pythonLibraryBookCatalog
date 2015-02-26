__author__ = 'carlo'
from mongoengine import *
from book import *

class Library(Document):

    name = StringField(max_length=200, required=True)
    address = StringField(max_length=200)
    manager = StringField(max_length=200)
    book = ListField(ReferenceField(Book))

class newLibrary:

    def display(self):
        print self.name
        print self.address
        print self.manager

    def __init__(self, name, address, manager):
        self.name = name
        self.address = address
        self.manager = manager