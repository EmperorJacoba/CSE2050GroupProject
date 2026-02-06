from student import Student

class Course:
    """
    A representation of a course at a university.\n
    Member variables:\n
    course_code: The course ID for this course. (e.g. "CSE 1010", "UNIV 1784", "MATH 1132Q")\n
    students: A list of Students enrolled in this course.
    """

    def __init__(self, course_code: str, credits: int, students: list[Student]):
        """
        Creates a new course that represents a course in the university catalog.
        :param course_code: the unique ID of the course (e.g. "CSE 1010", "UNIV 1784").
        :param credits: number of credits earned for completing the course.
        :param students: list of all students enrolled in this course.
        """

        pass

    def add_student(self, student: Student):
        """Add a student to this course's student roster."""
        pass

    def get_student_count(self) -> int:
        """Get the number of students currently enrolled in this course."""
        pass