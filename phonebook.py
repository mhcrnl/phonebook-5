#!/usr/bin/python
"""
Adaugarea unei clase Contact pentru pastrarea contactelor.
object - mostenirea din clasa obiect
"""

class Contact(object):
        """
        Functia care initializeaza obiectul Contact(constructor).
        """
        def __init__(self, nume=None, prenume=None, nrTel=None):
                self.nume = nume
                self.prenume = prenume
                self.nrTel = nrTel

        def __str__(self):
                """
                Functia string pt afisarea contactului
                """
                return "%s %s : %s" (self.nume, self.prenume, self.nrTel)

# Define lists, dicts, functions etc.
f = open('phonedata.txt', 'r')
book = eval(f.readline())
menu = ['A - Add a person/number', 'D - Delete a person/number', 'P - Print out phonebook']
"""
Adaugarea unei liste in care adaugam contactele
"""
contacte = []
# Print functions
def printNames(dic):
	print "Names in book: "
	for i in sorted(book):
		print i

def printContent(dic):
	print "Phonebook content: "
	for name, phone in sorted(dic.iteritems()):
		print name + " : " + phone

def printMenu(list):
	print "What do you want to do?"
	for i in menu:
		print i

# Menu functions		
def computeMenu(userInput):
	if userInput == "a" or userInput == "d" or userInput == "p":
		if userInput == "a":
			addItem1()
		elif userInput == "d":
			delItem()
		else:
			printContent(book)
	else:
		print "You didn't make a choise..."

# Functions of menu actions
def addItem():
	name = raw_input("Name: ")
	number = raw_input("Number: ")
	book[name] = number
	print ""
	printContent(book)
"""
Functia de adaugare a contactelor -vers 1
"""
def addItem1():
        print 'Introduceti numele contactului: '
        nume = raw_input()
        print 'Introduceti prenumele contactului: '
        prenume = raw_input()
        print 'Introduceti numarul de telefon: '
        nrTel = raw_input()
        # Clasa Contact care creaza obiectul ce va fi adaugata in lista.
        contact = Contact(nume, prenume, nrTel)
        # Lista de contacte in care se adauga contactul.
        contacte.append(contact)
        

def delItem():
	name = raw_input("Name: ")
	if name in book:
		del book[name]
		printContent(book)
	else:
		print "This name isn't in the book"

# Start of main program
printMenu(menu)
menuInput = raw_input("").lower()
computeMenu(menuInput)
