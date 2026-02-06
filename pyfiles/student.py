from course import Course

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

    def __init__(self, student_id: str, name: str, courses: dict):
        """
        Create a new student with its related information.
        :param student_id: Student's unique identifier.
        :param name: Student's name.
        :param courses: Dictionary of all courses the student has taken/is taking.
                        Key: the course at hand (as a Course object).
                        Value: The letter grade of the student. (e.g. "A", "B+").
        """
        pass

    def enroll(self, course: Course, grade: float) -> None:
        """
        Enroll a student in a given course with a specified grade. Updates the corresponding course to match.
        :param course: The course to enroll the student in.
        :param grade: The student's received grade in the course.
        """
        pass

    # Create an overload that allows for entering grade as a number, and convert that to a letter grade.
    # Why are we storing this as a string anyway? Can't this be the other way around? SMH
    def update_grade(self, course: Course, grade: str) -> None:
        """
        Modify the student's grade in a given course. No action taken if the student is not enrolled in the given Course.
        :param course: The specified course.
        :param grade: The new grade to assign to the student for this course.
        """
        pass

    def calculate_gpa(self) -> float:
        """
        Calculate the grade-point average of the student.
        :return: GPA, as a floating point number to two degrees of precision.
        """
        pass


    def get_courses(self) -> list[Course]:
        """
        Get a list of all courses this student is taking.
        """
        pass

    def get_course_info(self) -> str:
        """
        Generate a summary of this student's enrollments, including course code, grade, and credits.
        :return:
        """
        pass
