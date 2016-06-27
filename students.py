from peewee import *
# from playhouse.db_url import connect

# SQLite connection
# db = SqliteDatabase('students.db')

# MySQL connection
db = MySQLDatabase("students", user="root", passwd="pass123")

# host="127.0.0.1:3306"
# payhouse.db_url appraoch
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

students = [
	{'username': 'alexpeck',
	'points': 4888},
	{'username': 'chalkers',
	'points': 11912},
	{'username': 'kennethlove',
	'points': 4079},
	{'username': 'joeschmoe',
	'points': 407029},
	{'username': 'davemcfarland',
	'points': 14172}
]

def add_students():
	"""Function to add students to the database"""
	# loop through the students list/dict
	for student in students:
		# try to insert the student
		try:
			# Use the Student class to create entries in the database
			Student.create(username=student['username'],
					   points=student['points'])
		except IntegrityError:
			student_record = Student.get(username=student['username'])
			student_record.points = student['points']
			student_record.save()


if __name__ == '__main__':
	db.connect()
	db.create_tables([Student], safe=True)
	# add students to the database
	add_students()
	# safe=True is like IF EXISTS or IF NOT EXISTS