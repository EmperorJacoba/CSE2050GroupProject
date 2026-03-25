import sys
import csv_parser
from enrollmentrecord import EnrollmentRecord
from university import University

def print_menu_v2():
    menu = """
[Options (Milestone 2)]
a: View student data
b: Add student
c: View/Edit course data 
q: Quit
    """
    print(menu)

def prompt():
    """
    Displays a menu of options as well as giving the user the ability to select one of the options.

    Created By Justin Elak
    """
    print_menu_v2()
    menu_input = input("\nSelect a menu option: ").lower()

    match menu_input:
        case "a":
            print_student_data_filter(
                input("\tEnter student ID: ")
            )

        case "b":
            add_student_data()

        case "c":
            print_course_data_filter(
                input("\tEnter course ID: ")
            )

        case "q":
            return

        case _:
            print("Invalid Input, try again.")

    prompt()

def print_student_data_filter(student_id):
    if student := university.get_student(student_id):
        print_student_data(student)
    else:
        print("Invalid student ID.")

    input("Hit enter to exit back to menu.")

def print_student_data(student):
    data_formatted = f"""
Student {student.student_id}. ({student.name}):
GPA: {student.calculate_gpa()}
Enrolled courses:
{student.get_course_info_no_formatting()}
"""

    print(data_formatted)

def add_student_data():
    pass

def print_course_data_filter(course_id):
    if course := university.get_course(course_id):
        print_course_data(course)
    else:
        print("Invalid course ID.")

    input("Hit enter to exit back to menu.")

def print_course_data(course):
    data_formatted = f"""
Course {course.course_code}. {course.credits} credits.
Capacity: {course.capacity}. Number of students on waitlist: {len(course.waitlist)}

Statistics:
Mean: {course.get_mean_grade_point():.2f}
Median: {course.get_median_grade_point():.2f}
Mode: {course.get_mode_grade_point():.2f}

Show course waitlist and roster? (y/n)
"""
    print(data_formatted)

    yn = input()
    if yn.strip() == "y":
        print(format_waitlist(course))
        print(format_student_list(course.enrollments))

        while True:
            sort = input(f"""
            Sort by different method? Currently sorted by {course.enrolled_sorted_by}.
            Enter "id", "name" or "date". If not, use any other string to exit.
            """)

            if sort not in ["id", "name", "date"]:
                break
            else:
                course.sort_enrolled(sort, "insertion")
                print(format_student_list(course.enrollments))

    yn = input("Edit course information?")
    if yn.strip() == "y":
        edit_course_info(course)

def edit_course_info(course):
    menu = f"""
[Edit options for course {course.course_id}]
a: Enroll student
b: Drop student
q: exit
    """
    print(menu)
    menu_input = input("\nSelect a menu option: ").lower()
    match menu_input:
        case "a":
            if student := university.get_student(
                    input(
                        "Enter student ID to enroll. "
                    )
            ):
                course.request_enroll(student)
            else:
                "Invalid student id."
        case "b":
            if student := university.get_student(
                    input(
                        "Enter student ID to enroll. "
                    )
            ):
                course.drop(student)
        case _:
            return

    print()
    edit_course_info(course)

def format_waitlist(course):
    output_string = "Waitlist: "
    for i in course.waitlist.peek_all():
        output_string += f", {i.student_id} ({i.name})"
    return output_string

def format_student_list(list_enrollments: list[EnrollmentRecord]):
    output_string = ""
    for i in list_enrollments:
        output_string += f"{i.get_property("id"): {i.get_property("name")} Enrolled {i.get_property("date")}}"
    return output_string

if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise ValueError(
            "Incorrect number of command-line arguments passed to script. Please provide two .csv_files files: a .csv_files file with "
            "course data and .csv_files file with university/student data."
        )
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
                prompt()
                break
            case _:
                print("Invalid Input, try again.")
                user_input = input("Would you like to view more options? [y/n]: ").lower()

# <editor-fold desc="Old">

def print_menu():
    """
    Prints out a menu of university data options.

    Created by Justin Elak
    """
    print("\n[Options]")
    print("a: Get list of students in course")
    print("b: Get student GPA")
    print("c: Print student course data")
    print("d: Print common students in two courses")
    print("e: Print mean/med/mode for a course")
    print("q: Quit")


def get_students_in_course():
    """
    Prints all the names of the students in the course given by the user.

    Created By Justin Elak
    """
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
    """
    Prints the GPA of the student given by the user.

    Created by Justin Elak
    """
    while True:
        student_input = input("Student ID (Example:STU12345):")
        if not university.get_student(student_input):
            print("Student ID does not exist, please try another ID.")
        else:
            university.get_student(student_input).print_gpa()
            input("Hit enter to exit:")
            return

def print_student_course_data():
    """
    Prints out the course data for the student given by the user.

    Created By Justin Elak
    """
    while True:
        student_input = input("Student ID (Example:STU12345):")
        if not university.get_student(student_input):
            print("Student ID does not exist, please try another ID.")
        else:
            print(university.get_student(student_input).get_course_info())
            input("Hit enter to exit:")
            return

def print_common_students():
    """
    Prints out the student intersect between two courses give by the user.

    Created By Justin Elak
    """
    while True:
        course1_input = input("Course1, Course Code:")
        course2_input = university.get_course(input("Course2, Course Code:"))

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
    """
    Prints out course grade information for the course given by the user.

    Created By Justin Elak
    """
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

# </editor-fold>