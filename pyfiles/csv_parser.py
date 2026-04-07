# Entry point
# "Read student data and course data from the CSV files and create necessary objects and store those objects in a University Object."
# "In Student info, courses and grade
#
# s are given as a course code1:grade1;course code2:grade2;"

from student import Grade
from university import University
import csv

#Reads course info from course_catalog.csv_files and adds courses with credits to university object
def read_course_data(uni: University, path: str) -> None:
    """
    Read data from csv_files file of university course information and adds courses with credits to the given university object.
    :param uni: University object.
    :param path: A string with the path to the chosen csv_files file containing course data.

    Created by Justin Elak
    """
    with open(path, "r", newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            course_code = row["course_code"]
            course_credits = int(row["credits"])
            uni.add_course(course_code, course_credits)

def read_uni_data(uni: University, path: str) -> None:
    """
    Read data from csv_files file of university student information and enroll students into courses with the corresponding grades.
    :param uni: University object.
    :param path: A string with the path to the chosen csv_files file containing student data.

    Created by Justin Elak
    """

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

def read_course_capacity_data(uni: University, path: str):
    """
    Takes a university object and a path to capacity data CSV and updates course capacity information
    :param uni:
    :param path:
    :return:

    Created by Justin Elak
    """
    with open(path, "r", newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            course_code = row["course_id"]
            course_credits = int(row["credits"])
            course_capacity = int(row["capacity"])

            uni.add_course(course_code, course_credits, course_capacity)

def read_enrollment_data(uni: University, path: str):
    """
    Takes a university object and a path to enrollment data CSV and updates student and course information
    :param uni:
    :param path:
    :return:

    Created by Justin Elak
    """
    with open(path, "r", newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            student = uni.get_student((row["student_id"]))
            course = uni.get_course(row["course_id"])
            if not student:
                raise ValueError("Student does not exist")
            if not course:
                raise ValueError("Course does not exist")

            course.request_enroll(student)

if __name__ == "__main__":
    direct = "csv_files/"
    catalog = direct+"course_catalog_CSE10_with_capacity.csv"
    enrollments = direct+"enrollments_CSE10.csv"
    university_data = direct+"university_data.csv"
    course = direct+"course_catalog.csv"

    test_university = University()
    read_course_data(test_university, course)
    read_course_capacity_data(test_university, catalog)
    read_uni_data(test_university, university_data)
    read_enrollment_data(test_university, enrollments)

    for course in test_university.courses:
        course = test_university.get_course(course)
        print("Course:", course.course_code)
        for student in course.enrollments:
            print(student.student.student_id, end=", ")
        print()
        print("Waitlist:")
        while not course.waitlist.is_empty():
            print(course.waitlist.dequeue().student_id, end=", ")
        print()
        print()