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

def view_entries():
	"""View previous entries."""


def delete_entry(entry):
	"""Delete an entry."""

# add items as a list of tuples
# remember to place this in the script on a line that comes after I've defined the functions
# We're using an OrderedDict as an "alternate switch" an alternate switch is a programming concept that's not natively supported in Python so we're creating a workaround
menu = OrderedDict([
	('a', add_entry),
	('v', view_entries) # did not add a comma
])

if __name__ == '__main__':
	initialize()
	menu_loop()