import datetime

from enrollmentrecord import EnrollmentRecord
from data_types import LinkedQueue
from student import Student, Grade
import sorting

class Course:
    """
    A representation of a course at a university.\n
    Member variables:\n
    course_code: The course ID for this course. (e.g. "CSE 1010", "UNIV 1784", "MATH 1132Q")\n
    students: A list of Students enrolled in this course.
    """

    def __init__(
            self,
            course_code: str,
            credits: int,
            enrollments: list[EnrollmentRecord] = None,
            capacity: int = 256
        ):
        """
        Creates a new course that represents a course in the university catalog.
        :param course_code: the unique ID of the course (e.g. "CSE 1010", "UNIV 1784").
        :param credits: number of credits earned for completing the course.
        :param enrollments: list of all students enrolled in this course.

        Created by Jacob Russell
        """
        if not course_code:
            raise ValueError("Course code must not be empty.")

        self.course_code = course_code
        self.credits = credits
        self.capacity = capacity
        self.waitlist = LinkedQueue()
        self.enrolled_sorted_by = None

        if enrollments is not None:
            self.enrollments = enrollments
        else:
            self.enrollments = []

    def find_student_from_id(self, student_id: str) -> Student:
        raise ArithmeticError("Please implement find student from id")

    def get_student_list(self) -> list[Student]:
        return [item.student for item in self.enrollments]

    def request_enroll(self, student: Student, grade: Grade = Grade("F"), enroll_date: datetime.date = datetime.date.today()):
        if student not in self.get_student_list() and len(self.enrollments) >= self.capacity:
            self.waitlist.enqueue(student)
        else:
            self._add_student(student, grade=grade, enroll_date=enroll_date)

    def _remove_student(self, student: Student) -> bool:
        raise ArithmeticError("Please implement remove student!!!")

    def _add_student(self, student: Student, grade: Grade = Grade("F"), enroll_date: datetime.date = None) -> None:
        """
        Add a student to this course's student roster.
        :param student: The student to add to the course.
        :param grade: A grade object representing the grade of the student in the course (if known). "F" (0.0 grade points) by default.
        If the student is already present in the roster, updates the grade of the student.

        Created by Jacob Russell
        """

        if student not in self.get_student_list():
            self.enrollments.append(EnrollmentRecord(student, enroll_date))
            student.enroll(self, grade)
        else:
            student.update_grade(self, grade)

    def get_student_count(self) -> int:
        """Get the number of students currently enrolled in this course."""
        return len(self.enrollments)

    def get_student_intersect(self, other_course: "Course") -> list[Student]:
        """
        Return the intersecting students between courses
        :param other_course: Another course object to compare with.
        :return: A list of all students that are in both courses.

        Created by Justin Elak
        """

        intersecting_students = []
        other_course_students = other_course.get_student_list()
        for student in self.get_student_list():
            if student in other_course_students:
                intersecting_students.append(student.student_id)

        return intersecting_students

    def get_mode_grade_point(self) -> float:
        """
        Calculate the mode grade point (conversion from letter to GPA grade point) in a course.
        For reference, mode is the most common element in a sequence.
        :return: The mode grade point among the student roster's grades.

        Created by Justin Elak
        """
        count_dictionary = {}

        for student in self.get_student_list():
            grade = student.get_course_grade_float(self)
            if grade in count_dictionary:
                count_dictionary[grade] = count_dictionary[grade] + 1
            else:
                count_dictionary[grade] = 1

        return max(count_dictionary, key=count_dictionary.get)

    def get_median_grade_point(self) -> float:
        """
        Get the median grade point (conversion from letter to GPA grade point) in a course.
        For reference, median is the center value in a sorted list of values. If length is even, the median is the two
        middle elements divided by two.
        :return: The median grade point of the student roster's grades.

        Created by Jacob Russell
        """
        grade_list = [student.get_course_grade_float(self) for student in self.get_student_list()]

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
        """
        Get the mean grade point (conversion from letter to GPA grade point) in a course.
        For reference, mean is the average value of numerical values in a list. A.K.A. sum(list) / length(list)
        :return: The mean/average grade point of the student roster grades.

        Created by Jacob Russell
        """
        grade_list = [student.get_course_grade_float(self) for student in self.get_student_list()]

        if not grade_list:
            return 0

        return sum(grade_list) / len(grade_list)

    def sort_enrolled(self, by: str, algorithm: str):
        self.enrollments = sorting.get_algorithm_method(algorithm)(self.enrollments, by)
        self.enrolled_sorted_by = by

    def get_student_enrollment_data(self, student_id):
        index = self.sort_and_find_student_index(student_id)
        if index < 0:
            raise ValueError(f"No student with ID {student_id} is enrolled in this course.")
        return self.enrollments[index]

    def sort_and_find_student_index(self, student_id):
        def recursive_binary_search(records, target_id, low=None, high=None) -> int:
            if low is None or high is None:
                low, high = 0, len(records) - 1
            if low > high:
                return -1

            if low == high:
                if records[low].get_property("id") == target_id:
                    return low

                return -1

            mid = (high - low) // 2

            if records[mid].get_property("id") == target_id:
                return mid
            elif records[mid].get_property("id") > target_id:
                return recursive_binary_search(records, target_id, low, mid - 1)
            else:
                return recursive_binary_search(records, target_id, mid + 1, high)

        if self.enrolled_sorted_by != "id":
            self.sort_enrolled("id", "insertion")

        return recursive_binary_search(self.enrollments, student_id)

    def drop(self, student_id: str, enroll_date_for_replacement: datetime.date = None):
        index = self.sort_and_find_student_index(student_id)
        if index == -1:
            raise ValueError(f"No student with ID {student_id} is enrolled in this course")
        self.enrollments.pop(index)

        if len(self.waitlist) > 0:
            student_to_enroll = self.waitlist.dequeue()
            self._add_student(student_to_enroll, enroll_date=enroll_date_for_replacement)