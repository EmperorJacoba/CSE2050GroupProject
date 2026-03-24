import datetime
import unittest
from course import Course
from student import Student, Grade
from data_types import LinkedQueue
from university import University

class TestLinkedQueue(unittest.TestCase):
    def setUp(self):
        self.queue = LinkedQueue()
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)

    def test_pop(self):
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.dequeue(), 3)
        self.assertRaises(IndexError, self.queue.dequeue)

    def test_len(self):
        self.assertEqual(len(self.queue), 3)
        self.queue.dequeue()
        self.assertEqual(len(self.queue), 2)

def make_dummy_course(grade_list: list[Grade]) -> Course:
    """
    Make a course with four pre-loaded students for easy data checks on them.
    :param grade_list: A list of four Grade objects for the four students to have
    :return: The dummy course with the four students with the given grades.

    Created by Jacob Russell
    """
    course = Course("CSE 2050", 3)

    student1 = Student("STU94146", "Justin")
    student2 = Student("STU28734", "Justin2")
    student3 = Student("STU94122", "Justin3")
    student4 = Student("STU94322", "Justin4")

    student1.enroll(course, grade_list[0])
    student2.enroll(course, grade_list[1])
    student3.enroll(course, grade_list[2])
    student4.enroll(course, grade_list[3])

    return course

class TestCourseMilestone2Features(unittest.TestCase):
    def setUp(self):
        self.capacity = 3
        self.credits = 3
        self.course_test = Course("TEST1100", self.credits, capacity=self.capacity)

        # Sorting orders
        # ID: 1,2,3
        # Name: 2,3,1
        # Date: 3,2,1
        self.student1 = Student("STU00001", "Clam")
        self.student2 = Student("STU00002", "Albert")
        self.student3 = Student("STU00003", "Brainiac")

        self.course_test.request_enroll(self.student1, enroll_date=datetime.date(2002, 1, 1))
        self.course_test.request_enroll(self.student2, enroll_date=datetime.date(2001, 1, 1))
        self.course_test.request_enroll(self.student3, enroll_date=datetime.date(2000, 1, 1))

    def test_init(self):
        self.assertEqual(self.course_test.course_code, "TEST1100")
        self.assertEqual(self.course_test.credits, self.credits)

        self.assertEqual(len(self.course_test.enrollments), self.capacity)
        self.assertEqual(self.course_test.get_student_list(), [self.student1, self.student2, self.student3])

        self.assertEqual(self.course_test.capacity, self.capacity)

    def test_sort_id(self):
        self.course_test.sort_enrolled("id", "insertion")
        self.assertEqual(self.course_test.enrolled_sorted_by, "id")
        self.assertEqual(self.course_test.get_student_list(), [self.student1, self.student2, self.student3])

        self.course_test.sort_enrolled("name", "bubble")
        self.assertEqual(self.course_test.enrolled_sorted_by, "name")
        self.assertEqual(self.course_test.get_student_list(), [self.student2, self.student3, self.student1])

        self.course_test.sort_enrolled("date", "insertion")
        self.assertEqual(self.course_test.enrolled_sorted_by, "date")
        self.assertEqual(self.course_test.get_student_list(), [self.student3, self.student2, self.student1])

    def test_duplicate_enroll(self):
        self.course_test.request_enroll(self.student1)
        self.assertEqual(len(self.course_test.get_student_list()), self.capacity)

    def test_drop_and_waitlist(self):
        # init students for waiting
        student4 = Student("STU00004", "Darryl")
        student5 = Student("STU00005", "Eclair")

        # Test dropping no waitlist
        self.assertEqual(len(self.course_test.waitlist), 0)

        self.course_test.drop("STU00001")
        self.assertEqual(len(self.course_test.get_student_list()), self.capacity - 1)

        self.assertEqual(self.course_test.get_student_list()[0], self.student2)
        self.assertEqual(self.course_test.get_student_list()[1], self.student3)

        self.assertEqual(len(self.course_test.waitlist), 0)

        # Reset
        self.course_test.request_enroll(self.student1, enroll_date=datetime.date(2002, 12, 12))

        # Test waitlist with two students
        self.course_test.request_enroll(student4, enroll_date=datetime.date(2005, 12, 12))
        self.course_test.request_enroll(student5, enroll_date=datetime.date(2006, 12, 12))

        self.assertEqual(self.course_test.waitlist.peek(), student4)
        self.assertEqual(len(self.course_test.waitlist), 2)

        # Test dropping and waitlist dequeue
        self.course_test.drop("STU00002", enroll_date_for_replacement=datetime.date(2010, 12, 13))
        self.assertEqual(self.course_test.get_student_list(), [self.student3, self.student1, student4])

        self.assertEqual(len(self.course_test.waitlist), 1)
        self.assertEqual(self.course_test.waitlist.peek(), student5)

        # Test enroll replacement date
        self.assertEqual(
            self.course_test.get_student_enrollment_data("STU00004").enroll_date,
            datetime.date(2010, 12, 13)
        )

    def test_binary_search(self):
        # Unassigned student ID
        self.assertEqual(self.course_test.sort_and_find_student_index("STU00005"), -1)

        # Assigned student ID. First one added (self.student1)
        self.assertEqual(self.course_test.sort_and_find_student_index("STU00001"), 0)

    def test_get_mode(self):
        """
        Test Course.get_mode_grade_point() to check it correctly returns the mode of added grades.

        Created by Jacob Russell
        """
        course = make_dummy_course([Grade("A"), Grade("A"), Grade("B"), Grade("C")])

        self.assertEqual(4.0, course.get_mode_grade_point())

    def test_get_median(self):
        """
        Test Course.get_median_grade_point() to check it correctly gets the median grade point of added grades. Also
        checks if it works for when the length is even AND when it is odd.

        Created by Jacob Russell
        """
        course = make_dummy_course([Grade("A"), Grade("A"), Grade("B"), Grade("C")])

        self.assertEqual((4.0 + 3.0) / 2, course.get_median_grade_point())

        student5 = Student("STU12111", "Irrelevant")
        student5.enroll(course, Grade("D"))

        self.assertEqual(3.0, course.get_median_grade_point())

    def test_get_mean(self):
        """
        Test Course.get_mean_grade_point() to check it correctly calculates the average grade point of added grades.

        Created by Jacob Russell
        """
        course = make_dummy_course([Grade("A"), Grade("A"), Grade("B"), Grade("C")])

        self.assertEqual((4.0 + 4.0 + 3.0 + 2.0) / 4, course.get_mean_grade_point())

class TestStudentMilestone2(unittest.TestCase):
    def setUp(self):
        self.student = Student("STU10000", "Alex")
        self.course1 = Course("MATH 1132Q", 4)
        self.course2 = Course("EPSY 1100", 4)

    def test_init(self):
        self.assertEqual(self.student.student_id,"STU10000")
        self.assertEqual(self.student.name, "Alex")
        self.assertEqual(self.student.courses, {})

    def test_enroll(self):
        self.student.enroll(self.course1, Grade("A"))
        self.assertEqual(self.student.courses, {self.course1 : Grade("A")})
        self.assertEqual(self.course1.get_student_list(), [self.student])

    def test_calculate_gpa(self):
        self.student.enroll(self.course1, Grade("A"))
        self.student.enroll(self.course2, Grade("B+"))

        expected_gpa = (4*4 + 4*3.3) / 8

        self.assertEqual(self.student.calculate_gpa(), expected_gpa)

    def test_get_course_info(self):
        self.student.enroll(self.course1, Grade("A"))
        self.assertEqual(self.student.get_course_info().split("\n")[1], "Course: MATH 1132Q, Credits: 4, Grade: A")

if __name__ == "__main__":
    unittest.main()




