from peewee import *
# from playhouse.db_url import connect

# SQLite connection
# db = SqliteDatabase('students.db')

# MySQL connection
db = MySQLDatabase("students", user="root", passwd="pass123")

# host="127.0.0.1:3306"
# db = connect('mysql://root:pass123@127.0.0.1:3306/students')


class Student(Model):
	# Always make the model name singular, because
	# the model represents a single item in the database
	username = CharField(max_length=255, unique=True)
	points = IntegerField(default=0)

	class Meta:
		# This isn't a metaclass, it's just a class 
		# named Meta
		database = db

if __name__ == '__main__':
	db.connect()
	db.create_tables([Student], safe=True)
	# safe=True is like IF EXISTS or IF NOT EXISTS