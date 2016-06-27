from peewee import *
import MySQLdb

# SQLite connection
# db = SqliteDatabase('students.db')

# MySQLdb connection
db = MySQLdb.connect(host="localhost", 
					 user="root", 
					 passwd="123pass", 
					 db="students")

cursor = db.cursor()

# execute SQL select statement
# cursor.execute("SELECT * FROM LOCATION")

# commit your changes
# db.commit()

# get the number of rows in the resultset
# numrows = int(cursor.rowcount)

# get and display one row at a time
# for x in range(0,numrows):
# 	row = cursor.fetchone()
# 	print row[0], "-->", row[1]

# close the database connection
# db.close()

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