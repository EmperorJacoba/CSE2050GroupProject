# Entry point
# "Read student data and course data from the CSV files and create necessary objects and store those objects in a University Object."
# "In Student info, courses and grade
#
# s are given as a course code1:grade1;course code2:grade2;"

from student import Grade
from university import University
import csv

university1 = University({},{})

#Reads course info from course_catalog.csv and adds courses with credits to university object
with open("csv/course_catalog.csv", "r", newline='') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        course_code = row["course_code"]
        course_credits = int(row["credits"])
        university1.add_course(course_code,course_credits)

#Reads students information from university_data.csv and enrolls students into university object
with open("csv/university_data.csv", "r", newline='') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        student_id = row["student_id"]
        student_name = row["name"]
        university1.add_student(student_id, student_name)

#Reads student info from university_data.csv and enrolls students into courses with corresponding grades
with open("csv/university_data.csv", "r", newline='') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        student_id = row["student_id"]
        student_name = row["name"]
        courses = row["courses"].split(';')
        grades = {}

        student = university1.add_student(student_id, student_name)

        #Create dict with course and grades
        for course in courses:
            course_detail = course.split(":")
            grades[course_detail[0]] = course_detail[1]

        #Enroll students into course with grade from dict
        for course in grades:
            student.enroll(university1.get_course(course), Grade(grades[course]))