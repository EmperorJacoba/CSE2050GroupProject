class Grade:
    """
    A representation of a letter grade. Can be instantiated as a letter grade, integer grade, or decimal grade
    and can be converted to a grade point easily with get_grade_point().
    """

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
        """

        if isinstance(grade_id, str):
            if grade_id in Grade.GRADE_POINTS.keys():
                self.grade = grade_id
            else:
                self.grade = 'F'
                print(f"Invalid grade letter assignment was attempted. "
                      f"Invalid grade letter attempt: '{grade_id}' "
                      f"Grade assigned instead was '{self.grade}'.\n"
                      f"Please retry the operation with a valid decimal number from 0-100 "
                      f"or valid letter grade as given in the README.")

        elif isinstance(grade_id, float) or isinstance(grade_id, int):
            grade_id = round(grade_id, 2) # 2 decimals to conform to the NUMBER_TO_GRADE_ID dict

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
            print(f"Failed: {grade_id}, {type(grade_id)}")


    def get_grade_point(self) -> float:
        return Grade.GRADE_POINTS[self.grade]

    def __str__(self):
        return self.grade

    def __eq__(self, other):
        return other.grade == self.grade

    def __float__(self):
        return Grade.GRADE_POINTS[self.grade]


def validate_student_id(student_id: str) -> bool:

    err_string = ""

    if len(student_id) != 8:
        err_string += f"Student ID {student_id} is invalid. ID string must be eight characters\n"

    if student_id[0:3] != "STU":
        err_string += f"Student ID {student_id} is invalid. ID string must start with \"STU\".\n"

    if err_string != "":
        raise ValueError(err_string)

    return True

class Student:
    """
    A representation of a given student at a University.\n

    Member variables:\n
    student_id: The student's unique identification string. Formatted as STUXXXXX. Example: "STU12345" "STU12EK4"\n
    name: The name of the student.\n
    courses: Dictionary of all courses the student has taken/is taking.
        Key: the course at hand (as a Course object).
        Value: The letter grade of the student. (e.g. "A", "B+").
    """

    def __init__(self, student_id: str, name: str, courses: dict = None):
        """
        Create a new student with its related information.
        :param student_id: Student's unique identifier.
        :param name: Student's name.
        :param courses: Dictionary of all courses the student has taken/is taking.
                        Key: the course at hand (as a Course object).
                        Value: The letter grade of the student. (e.g. "A", "B+").
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

    # Use a grade class (setup below) to store and validate grades from string
    # Allows easy storage, calculation, conversion of grades. Convert from string formatted like "A+" or float like 98.0
    # Overloads for these!
    def enroll(self, course, grade: Grade) -> None:
        """
        Enroll a student in a given course with a specified grade. Updates the corresponding course to match.
        :param course: The course object to enroll the student in.
        :param grade: The student's received grade in the course, as a Grade object.
        """

        if isinstance(grade, str):
            grade = Grade(grade)

        if course not in self.courses.keys():
            self.courses[course] = grade

        course.add_student(self, grade)

    def update_grade(self, course, grade: Grade) -> None:
        """
        Modify the student's grade in a given course. No action taken if the student is not enrolled in the given Course.
        :param course: The specified course.
        :param grade: The new grade to assign to the student for this course.
        """

        if course in self.courses.keys():
            self.courses[course] = grade

    def get_course_grade_str(self, course) -> str:
        return self.courses[course]

    def get_course_grade_float(self, course) -> float:
        return float(self.courses[course])

    def calculate_gpa(self) -> float:
        """
        Calculate the grade-point average of the student.
        :return: GPA, as a floating point number to two degrees of precision.
        """

        grade_points = 0
        credits = 0

        for (key, value) in self.courses.items():
            credits += key.credits
            grade_points += value.get_grade_point()

        if credits == 0:
            return 0

        raw_gpa = (grade_points * credits) / credits

        return round(raw_gpa, 2)

    def print_gpa(self) -> None:
        print(self.calculate_gpa())

    def get_courses(self) -> list:
        """
        Get a list of all courses this student is taking.
        """

        return list(self.courses.keys())

    def get_course_info(self) -> str:
        """
        Generate a summary of this student's enrollments, including course code, grade, and credits.
        """

        output_string = f"Enrolled courses for {self.name}. (ID: {self.student_id})\n"
        for course, grade in self.courses.items():
            output_string += f"Course: {course.course_code}, Credits: {course.credits}, Grade: {grade}\n"

        output_string += f"\nStudent's GPA: {self.calculate_gpa()}"
        return output_string