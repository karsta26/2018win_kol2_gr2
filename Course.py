import numpy as np

class Course(object):

	def __init__(self, name):
		self.list_of_students = []
		self.attendance_of_students = {}
		self.scores_of_students = {}
		self.name = name

	def add_student(self, student):
		self.list_of_students.append(student)
		self.attendance_of_students[student] = 0
		self.scores_of_students[student] = []

	def add_score(self, student, score):
		self.scores_of_students[student].append(score)

	def add_attendance(self, student):
		self.attendance_of_students[student] += 1

	def get_all_students_average_score(self):
		all_grades = []
		for student, grades in self.scores_of_students.items():
			for grade in grades:
				all_grades.append(grade)
		
		return np.mean(all_grades)

	def get_student_average_score(self, student):
		grades = self.scores_of_students[student]
		return np.mean(grades)

	def total_attendance_of_students(self):
		total_attendance = 0
		for student, attendance in self.attendance_of_students.items():
			total_attendance += attendance

		return total_attendance