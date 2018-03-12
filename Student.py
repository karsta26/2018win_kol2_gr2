class Student(object):
	
	def __init__(self, name, surname):
		self.name = name
		self.surname = surname

	def __str__(self):
		return 'Student {} {}'.format(self.name, self.surname)
