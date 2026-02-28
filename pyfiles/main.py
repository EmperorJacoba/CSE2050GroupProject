import sys
import csv_parser
from university import University

def print_menu():
    print("a: Get list of students in course")
    print("b: Get student GPA")
    print("c : Print student course data")
    print("d : Print common students in two courses")
    print("e: Print mean/med/mode for a course")
    print("q: Quit")

def prompt_user():
    print_menu()
    user_input = input("Select a menu option: ")
    while user_input != "q":
        match user_input:
            case "a":
                pass
            case "b":
                pass
            case "c":
                pass
            case "d":
                pass
            case "e":
                pass
            case _:
                print("Invalid Input, try again.")
                print_menu()
                user_input = input("Select a menu option: ")

course_cat = sys.argv[1]
student_data = sys.argv[2]

university = University()
csv_parser.read_course_data(university, course_cat)
csv_parser.read_uni_data(university, student_data)

print(f"Median GPA: {university.get_median_gpa()}")
print(f"Mean GPA: {university.get_mean_gpa()}")

user_input = input("Would you like to view more options? [y/n]: ").lower()
while user_input != "n":
    match user_input:
        case "y":
            prompt_user()
        case _:
            print("Invalid Input, try again.")
            user_input = input("Would you like to view more options? [y/n]: ").lower()