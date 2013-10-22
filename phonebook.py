# Define lists, dicts, functions etc.
f = open('phonedata.txt', 'r')
book = eval(f.readline())
menu = ['A - Add a person/number', 'D - Delete a person/number', 'P - Print out phonebook']


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
			addItem()
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