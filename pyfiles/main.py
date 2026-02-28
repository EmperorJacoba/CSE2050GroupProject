import sys
import csv_parser
from university import University

def print_menu():
    print("\n[Options]")
    print("a: Get list of students in course")
    print("b: Get student GPA")
    print("c: Print student course data")
    print("d: Print common students in two courses")
    print("e: Print mean/med/mode for a course")
    print("q: Quit")

def prompt_user():
    menu_input = None
    while menu_input != "q":
        print_menu()
        menu_input = input("Select a menu option: ").lower()
        match menu_input:
            case "a":
                get_students_in_course()

            case "b":
                get_student_gpa()

            case "c":
                print_student_course_data()

            case "d":
                print_common_students()

            case "e":
                print_course_grade_stats()

            case "q":
                pass
            case _:
                print("Invalid Input, try again.")
def get_students_in_course():
    while True:
        user_course = input("Course Code:")
        if not university.get_course(user_course):
            print("Course does not exist, please try another course.")
        else:
            print("\nStudents in", user_course)
            university.print_students_in_course(user_course)
            input("Hit enter to exit:")
            return

def get_student_gpa():
    while True:
        student_input = input("Student ID (Example:STU12345):")
        if not university.get_student(student_input):
            print("Student ID does not exist, please try another ID.")
        else:
            university.get_student(student_input).print_gpa()
            input("Hit enter to exit:")
            return

def print_student_course_data():
    while True:
        student_input = input("Student ID (Example:STU12345):")
        if not university.get_student(student_input):
            print("Student ID does not exist, please try another ID.")
        else:
            print(university.get_student(student_input).get_course_info())
            input("Hit enter to exit:")
            return

def print_common_students():
    while True:
        course1_input = input("Course1, Course Code:")
        course2_input = university.get_course(input("Course1, Course Code:"))

        if not university.get_course(course1_input):
            print("Course1's Course Code, does not exist try again.")
        elif not course2_input:
            print("Course2's Course Code, does not exist try again.")
        else:
            student_intersect = university.get_course(course1_input).get_student_intersect(course2_input)
            for student in student_intersect:
                print(student)
            input("Hit enter to exit:")
            return

def print_course_grade_stats():
    while True:

        course_input = university.get_course(input("Course Code:"))
        if not course_input:
            print("Course does not exist, please try another course.")
        else:
            print(f"[{course_input.course_code} grade stats]")
            print(f"Mean: {course_input.get_mean_grade_point():.2f}")
            print(f"Median: {course_input.get_median_grade_point():.2f}")
            print(f"Mode: {course_input.get_mode_grade_point():.2f}")
            input("Hit enter to exit:")
            return

course_cat = sys.argv[1]
student_data = sys.argv[2]

university = University()
csv_parser.read_course_data(university, course_cat)
csv_parser.read_uni_data(university, student_data)

print(f"Median GPA: {university.get_median_gpa():.2f}")
print(f"Mean GPA: {university.get_mean_gpa():.2f}")

user_input = input("Would you like to view more options? [y/n]: ").lower()
while user_input != "n":
    match user_input:
        case "y":
            prompt_user()
            break
        case _:
            print("Invalid Input, try again.")
            user_input = input("Would you like to view more options? [y/n]: ").lower()