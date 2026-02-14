from pyfiles.student import Student, Grade

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
        self.course_code = course_code
        self.credits = credits
        self.students = students

    def add_student(self, student: Student, grade: Grade = Grade("F")) -> None:
        """
        Add a student to this course's student roster.
        :param student: The student to add to the course.
        :param grade: A grade object representing the grade of the student in the course (if known). "F" (0.0 grade points) by default.
        If the student is already present in the roster, updates the grade of the student.
        """

        if student not in self.students:
            self.students.append(student)
            student.enroll(self, grade)
        else:
            student.update_grade(self, grade)

    def get_student_count(self) -> int:
        """Get the number of students currently enrolled in this course."""
        return len(self.students)