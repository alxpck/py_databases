from peewee import *

# MySQL connection
db = MySQLDatabase("diary", user="root", passwd="pass123")

class Entry(Model):
	# content
	# timestamp

	class Meta:
		database = db

def menu_loop():
	"""Show the menu"""


def add_entry():
	"""Add an entry."""


def view_entries():
	"""View previous entries."""


def delete_entry(entry):
	"""Delete an entry."""

if __name__ == '__main__':
	menu_loop()