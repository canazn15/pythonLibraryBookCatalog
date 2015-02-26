__author__ = 'carlo'

import sys
from main import *

class testcase:
    def runTestcase(self,num):
        try:
            # run the initialized database
            self.command = 1
            # grab input testcase_num.txt files for input
            sys.stdin = open('testcase_%(num)s.txt'%{'num':num}, 'rt')
            # run the menu with sys.stdin as input
            menu(self.db, self.database, self.command)
        except:
            sys.stdin.close()
            print "An error occurred during testcase"

    def __init__(self,db,database,command):
        self.db = db
        self.database = database
        self.command = command