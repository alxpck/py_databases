#!/usr/bin/env python
# stuff that comes from Python, alphabetized
from collections import OrderedDict
import datetime
import sys

# stuff that comes from a third-party, alphabetized
from peewee import *

# collections is a part of the standard Python library and 
# contains alternate datastructures like OrderedDicts and 
# named tuples and other things that you'd need to build
# programatically if you wanted to use them

# MySQL connection
db = MySQLDatabase("diary", user="root", passwd="pass123")

# This must match the name of the database table
# I changed it from Entry(Model) because I wanted the databaes in SQL to be plural since it contains multiple entries, but as I start to work with the code in Python now I want the class to be singular and the database to be plural, but if anything it's probably better to keep the Python code setup to match the singular/plural rules because that's what I'm actually interacting with as I query the database
class Entries(Model):
	# content
	# We're not using a VARCHAR because varchar's require a max length, and we don't want to explicitly define a limit. 
	content = TextField()
	# timestamp
	# when it creates a default it will call the now() function, but because we left off the parenthesis it only runs the function when the default is created.
	timestamp = DateTimeField(default=datetime.datetime.now)

	class Meta:
		database = db

def initialize():
	"""Create the database and the table if they don't exist."""
	db.connect()
	# different than the tutorial, but I like to make the tables plural of the things they will contain
	db.create_tables([Entries], safe=True)

def menu_loop():
	"""Show the menu"""
	# our way of setting a variable without giving it a value
	choice = None

	while choice != 'q':
		print("Enter 'q' to quit.")
		for key, value in menu.items():
			# a) Add an entry. 
			# dunder doc will pull the function docnotes, the things in triple quotes
			print('{}) {}'.format(key, value.__doc__))
		choice = input('Action: ').lower().strip()

		if choice in menu:
			# this is the tricky bit
			# it uses choice (a single letter) to pull up the corresponding function from the menu
			# the parenthesis at the end of menu[choice] are appended to the function name in menu? And/Or they are a trigger telling us to run whatever function is chosen by menu
			menu[choice]()

def add_entry():
	"""Add an entry."""
	print("Enter your entry. Press Control + D when finished.")
	# Sys's standard in stdin will pull in all the keyboard strokes that a user types (including a history of deleted characters?). The read function will read the results of standard in, and the strip function will stip out whitespace from either the front or the back of the data (but not from between words or characters). 
	data = sys.stdin.read().strip()

	# check to see if there is data, if there is...
	if data:
		# prompt the user for input with a statement asking if they'd like to save their input, use the lower function to lowercase the result, and use a conditional operator to only proceed if the input does not equal 'n'
		if input('Save entry? [Yn] ').lower() != 'n':
			Entries.create(content=data)
			print("Saved successfully!")

def view_entries(search_query=None):
	"""View previous entries."""
	# SELECT SQL, ORDER BY the timestamp we created in the Entries model / class when the entry is added to the database
	entries_list = Entries.select().order_by(Entries.timestamp.desc())

	# filter only if we're passed a search query
	if search_query:
		# set the entries list to be a subset of the the entries list where the entries contain the search query.
		# in SQL this would look like this --- SELECT * FROM entries WHERE content LIKE '%search_query%' ORDER BY timestamp DESC
		# There's a big part of me that would like to use a database handler for Python that lets me write plain SQL because then I get to strengthen my SQL muscles as well as my python muscles. And that makes me a more robust programmer. 
		entries_list = entries_list.where(Entries.content.contains(search_query))

	# iterate through the entries list
	for entry in entries_list:
		# convert the datetime objects to strings
		timestamp = entry.timestamp.strftime('%A %B %d, %Y %I:%M%p')
		# print the time string
		print(timestamp)
		# print "==========" a dividing line of equal signs that's the same length as the timestamp. This is a great hacky little shortcut for formatting
		print('='*len(timestamp))
		# print the content of the post. Just like we had access to the timestamp from the Entries class we also have access to the content. This is actually teaching me more about object-oriented design/programming than databases, but c'est la vie.
		print(entry.content)
		print('n) next entry') 
		print('q) return to main menu') # I feel like this should be 'r' and not 'q'

		# collect input from the user and save it as a variable after transforming it to lowercase and stripping white space from the front and end of the string
		# 'N' is capitalized because it's our default step, it's just a design nudge to the user that this is the default thing to do.
		next_action = input('Action: [Nq] ').lower().strip()
		if next_action == 'q':
			break # break our for loop
			# we don't have to explicitly program an action for 'n' because 'next entry' is handled by the for loop. Anything ('n', 'az' 'afja;f') that's not 'q' will move us on to the next entry. 
			# What would be nice from a user perspective is to know when we're at the last entry and send a message saying 'no more entries' instead of just showing blank entries/menus. 

def search_entries():
	"""Search the entries for a string."""
	# call the view entries function, and prompt the user for input which we pass into the view_entries function as the search query.
	# this is really smart and compact code compared to what I'm building. Especially in the way that user input is woven into the functions.
	view_entries(input('Search query: '))


def delete_entry(entry):
	"""Delete an entry."""

# add items as a list of tuples
# remember to place this in the script on a line that comes after I've defined the functions
# We're using an OrderedDict as an "alternate switch" an alternate switch is a programming concept that's not natively supported in Python so we're creating a workaround
menu = OrderedDict([
	('a', add_entry),
	('v', view_entries),
	('s', search_entries),
])

if __name__ == '__main__':
	initialize()
	menu_loop()