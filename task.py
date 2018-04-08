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
# If you can thing of any other features, you can add them.
# Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
# Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
# The goal of this task is for you to SHOW YOUR BEST python programming skills.
# Impress everyone with your skills, show off with your code.
#
# Your program must be runnable with command "python task.py".
# Show some usecases of your library in the code (print some things)

# - no classes
# - all data must be stored in dict {}
# - use library for math (avg)
# - store dict in file and you can read data and write
# - PEP 8
# - all functionality mentions in file
# - do not exceed 8 functions

import statistics
import json


def read_data_from_file():
    data = json.load(open('data.json'))
    return data


def write_data_to_file(school):
    with open('data.json', 'w') as outfile:
        json.dump(school, outfile)


def get_students_total_average_score(school):
    all_grades = []
    for student in school['students']:
        if 'classes' in student:
            for clas in student['classes']:
                if 'scores' in clas:
                    all_grades.extend(clas['scores'])
    return statistics.mean(all_grades)


def get_students_average_score_in_class(school, class_name):
    all_grades = []
    for student in school['students']:
        if 'classes' in student:
            for clas in student['classes']:
                if 'scores' in clas and clas['name'] == class_name:
                    all_grades.extend(clas['scores'])
    return statistics.mean(all_grades)


def get_total_attendance_of_students(school):
    total_attendance = 0
    for student in school['students']:
        if 'classes' in student:
            for clas in student['classes']:
                if 'attendance' in clas:
                    total_attendance += clas['attendance']

    return total_attendance


def add_student(school, name, surname):
    school['students'].append({'name': name, 'surname': surname})


def print_all_students(school):
    for student in school['students']:
        print('{} {}'.format(student['name'], student['surname']))
        if 'classes' in student:
            for clas in student['classes']:
                print('  {}'.format(clas['name']))
                if 'scores' in clas:
                    print('    scores: {}'.format(clas['scores']))
                if 'attendance' in clas:
                    print('    attendance: {}'.format(clas['attendance']))


def add_score_for_student(school, **kwargs):
    is_student = False
    try:
        score = int(kwargs['score'])
    except ValueError:
        print("Score should be number")
        return

    for student in school['students']:
        if student['name'] == kwargs['name'] and student['surname'] == kwargs['surname']:
            is_student = True
            if 'classes' in student:
                is_classes = False
                for clas in student['classes']:
                    if clas['name'] == kwargs['class_name']:
                        clas['scores'].append(score)
                        is_classes = True
                        print("Success")
                if is_classes is False:
                    new_class = {'name': class_name, 'scores': [score]}
                    student['classes'].append(new_class)
                    print("Success")

            else:
                student['classes'] = []
                new_class = {'name': class_name, 'scores': [score]}
                student['classes'].append(new_class)
                print("Success")
    if not is_student:
        print("No such student")


if __name__ == '__main__':
    school = read_data_from_file()
    menu = "\n\nWelcome to diary!\nChoose what you want to do\n1. Add student\n2. Print all students\n3. Read data " \
           "from file\n4. Save data to file\n5. Students total average score\n6. Students average score in class\n7. " \
           "Total attendance of students\n8. Add score for student\n To exit press q \n\n"
    print(menu)
    user_input = input("<number>: ")
    while user_input != 'q':
        if user_input == '1':
            print("Add new student")
            name = input("Enter name: ")
            surname = input("Enter surname: ")
            add_student(school, name, surname)
            print("Student added!")
        elif user_input == '2':
            print('List of all students:')
            print_all_students(school)
        elif user_input == '3':
            print("Reading data from file")
            school = read_data_from_file()
        elif user_input == '4':
            print("Saving data to file")
            write_data_to_file(school)
        elif user_input == '5':
            print("Student total average score: {}".format(get_students_total_average_score(school)))
        elif user_input == '6':
            clas = input("Enter name of class: ")
            try:
                print("Student average score in class {} is {}".format(clas, get_students_average_score_in_class(school,
                                                                                                                 clas)))
            except:
                print("There is no such classes")
        elif user_input == '7':
            print("Total attendance of students: {}".format(get_total_attendance_of_students(school)))
        elif user_input == '8':
            print("Add score for student")
            input_name = input("Enter name: ")
            input_surname = input("Enter surname: ")
            input_class_name = input("Enter class name: ")
            input_score = input("Enter score: ")
            add_score_for_student(school, name=input_name, surname=input_surname, class_name=input_class_name,
                                  score=input_score)

        print(menu)
        user_input = input("<number>: ")
