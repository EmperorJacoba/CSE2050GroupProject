from course import Course
from student import Student

class University:
    """
    A central manager of University data. Contains student data, course data, and methods to query data regarding both & enrollment.\n
    Member variables:\n
    students: A map of student IDs to Student objects.\n
    courses: A map of course codes to Course objects.
    """

    def __init__(self, students: dict[str, Student], courses: dict[str, Course]):
        """
        Create a new university, with a student and course directory.
        :param students: Dictionary of students enrolled in this University. Key = Student ID. Value = Student object.
        :param courses: Dictionary of courses this University offers. Key = Course Code/ID. Value = Course object.
        """
        self.students = students
        self.courses = courses

    def add_course(self, course_code: str, credits: int) -> Course:
        """
        Add a new course offering to this University.
        :param course_code: The course code of the course being added.
        :param credits: Number of credits given by taking this course.
        :return: The course object created with its corresponding properties
        """
        if course_code in self.courses.keys():
            return self.courses[course_code]

        new_course = Course(course_code, credits, [])
        self.courses[course_code] = new_course

        return new_course

    def add_student(self, student_id: str, name: str) -> Student:
        """
        Create a new representation of a student, with its ID and name, if not already enrolled.
        :param student_id: The 8 character ID for this student, formatted as STUXXXXX. Example: "STU12EO5"
        :param name: The name of the student being enrolled in the University.
        :return: The student object created with its corresponding properties.
        """

        if student_id in self.students.keys():
            return self.students[student_id]

        new_student = Student(student_id, name, {})
        self.students[student_id] = new_student

        return new_student

    def get_student(self, student_id: str) -> Student:
        """
        Get a student by ID, formatted as STUXXXXX.
        :param student_id: The ID of the student object being requested.
        :return: The student object with the specified ID. Returns None if the student does not exist.
        """
        if student_id in self.students:
            return self.students[student_id]
        else:
            return None
            # raise KeyError(f"Student with id {student_id} not registered at this university.")

    def get_course(self, course_code: str) -> Course:
        """
        Get the corresponding Course object for a given code.
        :param course_code: The course code of the Course object being requested.
        :return: The Course object with the specified code. Returns None if not found.
        """

        return self.courses.get(course_code)

    def get_course_enrollment(self, course_code: str) -> int:
        """
        Get the number of students enrolled in a given course.
        :param course_code: The course code of the Course object being queried.
        :return: The number of students enrolled in the specified course.
        """
        found_course = self.get_course(course_code)

        if found_course is None:
            return 0

        return len(found_course.students)

    def get_students_in_course(self, course_code: str) -> list[Student]:
        """
        Get a list of students enrolled in a given course.
        :param course_code: The course code of the Course object being queried.
        :return: A list of all students enrolled in the specified course.
        """

        found_course = self.get_course(course_code)

        if found_course is None:
            return []

        return found_course.students
