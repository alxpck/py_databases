#!/usr/bin/env python
import datetime
from peewee import *

# MySQL connection
db = MySQLDatabase("diary", user="root", passwd="pass123")

class Entry(Model):
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


def add_entry():
	"""Add an entry."""


def view_entries():
	"""View previous entries."""


def delete_entry(entry):
	"""Delete an entry."""

if __name__ == '__main__':
	initialize()
	menu_loop()