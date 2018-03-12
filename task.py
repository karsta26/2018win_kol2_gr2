# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.
#If you can thing of any other features, you can add them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)

from Student import Student
from Course import Course

if __name__ == '__main__':
	student1 = Student("Mike","Tyson")
	student2 = Student("Ann","Tiger")

	course1 = Course("Biology")
	course1.add_student(student1)
	course1.add_student(student2)

	course1.add_score(student1, 3)
	course1.add_score(student1, 5)
	course1.add_score(student2, 2)

	course1.add_attendance(student1)
	course1.add_attendance(student1)
	course1.add_attendance(student2)

	print(course1.get_all_students_average_score())
	print(course1.get_student_average_score(student1))
	print(course1.total_attendance_of_students())

