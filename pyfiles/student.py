import datetime


class Grade:
    """
    A representation of a letter grade. Can be instantiated as a letter grade, integer grade, or decimal grade
    and can be converted to a grade point easily with get_grade_point().
    """

    # Map of letter grade string to grade points
    GRADE_POINTS = {
        'A': 4.0,
        'A-': 3.7,
        'B+': 3.3,
        'B': 3.0,
        'B-': 2.7,
        'C+': 2.3,
        'C': 2.0,
        'C-': 1.7,
        'D': 1.0,
        'F': 0.0
    }

    # Map of grade percentages to letter grades to hundredth-place precision
    NUMBER_TO_GRADE_ID = {
        (0.00, 59.99): 'F',
        (60.00, 69.99): 'D',
        (70.00, 72.99): 'C-',
        (73.00, 76.99): 'C',
        (77.00, 79.99): 'C+',
        (80.00, 82.99): 'B-',
        (83.00, 86.99): 'B',
        (87.00, 89.99): 'B+',
        (90.00, 92.99): 'A-',
        (93.00, 100.00): 'A'
    }

    def __init__(self, grade_id):
        """
        Instantiate a new grade from a letter grade (formatted as "A", "B", etc) or from a number (ex. 80.67, 90)
        Assigns a default grade of 'F' if given value is invalid.

        Created by Jacob Russell
        """

        if isinstance(grade_id, str):
            if grade_id in Grade.GRADE_POINTS.keys():
                self.grade = grade_id
            else:
                self.grade = 'F'
                print(f"Invalid grade letter assignment was attempted. "
                      f"Invalid grade letter attempt: '{grade_id}' "
                      f"Grade assigned instead was '{self.grade}'.\n"
                      f"Please retry the operation with a valid integer or decimal number from 0-100 "
                      f"or valid letter grade as given in the README.")

        elif isinstance(grade_id, float) or isinstance(grade_id, int):
            grade_id = round(grade_id, 2) # 2 decimals to conform to the NUMBER_TO_GRADE_ID dict precision

            grade_match = ""
            for (range, value) in Grade.NUMBER_TO_GRADE_ID.items():
                if range[0] <= grade_id <= range[1]:
                    grade_match = value

            if not grade_match:
                self.grade = 'F'

                print(f"Invalid grade number assignment was attempted. "
                      f"Invalid grade number attempt: '{grade_id}' "
                      f"Grade assigned instead was '{self.grade}'.\n"
                      f"Please retry the operation with a valid decimal number from 0-100 "
                      f"or valid letter grade as given in the README.")
            else:
                self.grade = grade_match
        else:
            raise TypeError(f"Invalid grade_id type {type(grade_id)}. Grade must be inputted as string, int, or float.")

    def get_grade_point(self) -> float:
        """
        Convert the grade stored in a grade object to a GPA grade point.

        Created by Jacob Russell
        """
        return Grade.GRADE_POINTS[self.grade]

    def __str__(self):
        """
        Return letter grade representation of the grade.

        Created by Jacob Russell
        """
        return self.grade

    def __eq__(self, other):
        """
        Compares two grades based on the stored letter grade string.

        Created by Jacob Russell
        """
        return other.grade == self.grade

    def __float__(self):
        """
        Return the grade point representation of the stored grade data.

        Created by Jacob Russell
        """
        return Grade.GRADE_POINTS[self.grade]


def validate_student_id(student_id: str) -> bool:
    """
    Determine if a given student ID is valid. Raises an error if it is not valid, returns True otherwise.
    :param student_id: The given string meant to represent a student ID.
    :return: True if the ID is valid.

    Created by Jacob Russell
    """

    err_string = ""

    # ID is eight characters
    if len(student_id) != 8:
        err_string += f"Student ID {student_id} is invalid. ID string must be eight characters\n"

    # First three chars must be "STU".
    if student_id[0:3] != "STU":
        err_string += f"Student ID {student_id} is invalid. ID string must start with \"STU\".\n"

    # Alert user of errors determined in string ID (can be one or both)
    if err_string != "":
        raise ValueError(err_string)

    return True

# Note for course variables: there is no course type hinting for Course objects because course references student in some
# of its functions. Importing Course.py for use with type hinting results in a circular import error. Every time the name of
# a variable is "course", assume that it is a Course object.
class Student:
    """
    A representation of a given student at a University.\n

    Member variables:\n
    student_id: The student's unique identification string. Formatted as STUXXXXX. Example: "STU12345" "STU12EK4"\n
    name: The name of the student.\n
    courses: Dictionary of all courses the student has taken/is taking.
        Key: the course at hand (as a Course object).
        Value: The letter grade (e.g. "A", "B+") of the student as a Grade object.
    """

    def __init__(self, student_id: str, name: str, courses: dict = None):
        """
        Create a new student with its related information.
        :param student_id: Student's unique identifier.
        :param name: Student's name.
        :param courses: Dictionary of all courses the student has taken/is taking.
                        Key: the course at hand (as a Course object).
                        Value: The Grade object representing the grade of the student for that course.

        Created by Jacob Russell
        """

        if validate_student_id(student_id):
            self.student_id = student_id

        if len(name) == 0:
            raise ValueError("Student name must not be empty.")

        self.name = name

        if courses is not None:
            self.courses = courses
        else:
            self.courses = {}

    def __str__(self):
        return f"Student ID {self.student_id}: {self.name}, Courses: {self.courses.items()}"

    # Use a grade class (setup below) to store and validate grades from string
    # Allows easy storage, calculation, conversion of grades. Convert from string formatted like "A+" or float like 98.0
    # Overloads for these!
    def enroll(self, course, grade: Grade) -> None:
        """
        Enroll a student in a given course with a specified grade. Updates the corresponding course to match.
        :param course: The course object to enroll the student in.
        :param grade: The student's received grade in the course, as a Grade object.

        Created by Jacob Russell
        """

        if isinstance(grade, str):
            grade = Grade(grade)

        if course not in self.courses.keys():
            self.courses[course] = grade

        course.request_enroll(self, enroll_date=datetime.date.today())

    def update_grade(self, course, grade: Grade) -> None:
        """
        Modify the student's grade in a given course. No action taken if the student is not enrolled in the given Course.
        :param course: The specified course.
        :param grade: The new grade to assign to the student for this course, as a Grade object.

        Created by Jacob Russell
        """

        if course in self.courses.keys():
            self.courses[course] = grade

    def get_course_grade_str(self, course) -> str:
        """
        Get a string grade representation of the student's grade in a course. e.g. "A", "B+"
        :param course: The course object to query the grade for.
        :return: The string representation of the grade for the queried course.

        Created by Jacob Russell
        """
        return str(self.courses[course])

    def get_course_grade_float(self, course) -> float:
        """
        Get a GPA grade point representation of the student's grade in a course. e.g. 3.7, 2.0
        :param course: The course object to query the grade for.
        :return: The float (grade point) representation of the grade for the queried course.

        Created by Jacob Russell
        """
        return float(self.courses[course])

    def calculate_gpa(self) -> float:
        """
        Calculate the grade-point average of the student.
        :return: GPA, as a floating point number to two degrees of precision.

        Created by Jacob Russell
        """

        accumulated_grade_points = 0
        credits = 0

        for (key, value) in self.courses.items():
            accumulated_grade_points += (key.credits * value.get_grade_point())
            credits += key.credits

        if credits == 0:
            return 0

        raw_gpa = accumulated_grade_points / credits

        return round(raw_gpa, 2)

    def print_gpa(self) -> None:
        """
        Print the gpa of the student.

        Created by Jacob Russell
        """
        print(self.calculate_gpa())

    def get_courses(self) -> list:
        """
        Get a list of all courses this student is taking.

        Created by Jacob Russell
        """

        return list(self.courses.keys())

    def get_course_info(self) -> str:
        """
        Generate a summary of this student's enrollments, including course code, grade, and credits. Returns the summary
        as a string.

        Created by Jacob Russell
        """

        output_string = f"Enrolled courses for {self.name}. (ID: {self.student_id})\n"
        for course, grade in self.courses.items():
            output_string += f"Course: {course.course_code}, Credits: {course.credits}, Grade: {grade}\n"

        output_string += f"\nStudent's GPA: {self.calculate_gpa()}"
        return output_string