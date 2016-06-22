from peewee import *


# SQLite connection
# db = SqliteDatabase('students.db')

# MySQL connection
mysql_db = MySQLDatabase('my_students.db')

class BaseModel(Model):
	"""A base model that will use our MySQL database"""
	class Meta:
		database = mysql_db

class User(BaseModel):
	username = CharField()
	# etc etc