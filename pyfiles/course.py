from student import Student, Grade

class Course:
    """
    A representation of a course at a university.\n
    Member variables:\n
    course_code: The course ID for this course. (e.g. "CSE 1010", "UNIV 1784", "MATH 1132Q")\n
    students: A list of Students enrolled in this course.
    """

    def __init__(self, course_code: str, credits: int, students: list[Student] = None):
        """
        Creates a new course that represents a course in the university catalog.
        :param course_code: the unique ID of the course (e.g. "CSE 1010", "UNIV 1784").
        :param credits: number of credits earned for completing the course.
        :param students: list of all students enrolled in this course.
        """
        self.course_code = course_code
        self.credits = credits

        if students is not None:
            self.students = students
        else:
            self.students = []

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

    def get_student_intersect(self, other_course: "Course") -> list[Student]:
        """
        Return the intersecting students between courses
        :param other_course: Another course object to compare with.
        :return: A list of all students that are in both courses.
        """

        intersecting_students = []
        for student in self.students:
            if student in other_course.students:
                intersecting_students.append(student.student_id)
        return intersecting_students

    def get_mode_grade_point(self) -> float:
        count_dictionary = {}

        for i in self.students:
            grade = i.get_course_grade_float(self)
            if grade in count_dictionary:
                count_dictionary[grade] = count_dictionary[grade] + 1
            else:
                count_dictionary[grade] = 1

        return max(count_dictionary, key=count_dictionary.get)

    def get_median_grade_point(self) -> float:
        grade_list = [student.get_course_grade_float(self) for student in self.students]

        if not grade_list:
            return 0

        grade_list.sort()

        length = len(grade_list)
        middle_index = (length - 1) // 2

        if len(grade_list) % 2 == 0:
            return (grade_list[middle_index] + grade_list[middle_index + 1]) / 2
        else:
            return grade_list[middle_index]

    def get_mean_grade_point(self) -> float:
        grade_list = [student.get_course_grade_float(self) for student in self.students]

        if not grade_list:
            return 0

        return sum(grade_list) / len(grade_list)

