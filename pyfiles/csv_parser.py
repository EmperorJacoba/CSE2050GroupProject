# Entry point
# "Read student data and course data from the CSV files and create necessary objects and store those objects in a University Object."
# "In Student info, courses and grade
#
# s are given as a course code1:grade1;course code2:grade2;"

from student import Grade
from university import University
import csv

#Reads course info from course_catalog.csv and adds courses with credits to university object
def read_course_data(uni: University, path: str) -> None:
    """Read data from csv file of university course information and adds courses with credits to the given university object.
        :param uni: University object.
        :param path: A string with the path to the chosen csv file containing course data."""
    with open(path, "r", newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            course_code = row["course_code"]
            course_credits = int(row["credits"])
            uni.add_course(course_code,course_credits)

def read_uni_data(uni: University, path: str) -> None:
    """Read data from csv file of university student information and enroll students into courses with the corresponding grades.
        :param uni: University object.
        :param path: A string with the path to the chosen csv file containing student data."""

    with open(path, "r", newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            student_id = row["student_id"]
            student_name = row["name"]
            courses = row["courses"].split(';')
            grades = {}

            student = uni.add_student(student_id, student_name)

            #Create dict with course and grades
            for course in courses:
                course_detail = course.split(":")
                grades[course_detail[0]] = course_detail[1]

            #Enroll students into course with grade from dict
            for course in grades:
                student.enroll(uni.get_course(course), Grade(grades[course]))