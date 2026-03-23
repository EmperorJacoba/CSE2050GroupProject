import unittest
from course import Course
from student import Student
import datetime
from data_types import LinkedQueue


class TestLinkedQueue(unittest.TestCase):
    pass

class TestCourse(unittest.TestCase):

    def setUp(self):
        self.course_test = Course("TEST1100", 3, capacity=2)

        self.student1 = Student("STU00001", "Clam")
        self.student2 = Student("STU00002", "Albert")

        self.course_test.request_enroll(self.student1, enroll_date=datetime.date(1999, 1, 2))
        self.course_test.request_enroll(self.student2, enroll_date=datetime.date(2000, 1, 1))

    def test_init(self):
        self.assertEqual(self.course_test.course_code, "TEST1100")
        self.assertEqual(self.course_test.credits, 3)
        self.assertEqual(len(self.course_test.enrollments), 2)
        self.assertEqual(self.course_test.get_student_list(), [self.student1, self.student2])
        self.assertEqual(self.course_test.capacity, 2)

    def test_sort_id(self):
        self.course_test.sort_enrolled("id", "insertion")
        self.assertEqual(self.course_test.enrolled_sorted_by, "id")
        self.assertEqual(self.course_test.get_student_list(), [self.student1, self.student2])

        self.course_test.sort_enrolled("name", "bubble")
        self.assertEqual(self.course_test.enrolled_sorted_by, "name")
        self.assertEqual(self.course_test.get_student_list(), [self.student2, self.student1])

        self.course_test.sort_enrolled("date", "insertion")
        self.assertEqual(self.course_test.enrolled_sorted_by, "date")
        self.assertEqual(self.course_test.get_student_list(), [self.student1, self.student2])

    def test_duplicate_enroll(self):
        self.course_test.request_enroll(self.student1)
        self.assertEqual(len(self.course_test.get_student_list()), 2)

    def test_drop_and_waitlist(self):
        student3 = Student("STU00003", "Darryl")

        self.assertEqual(len(self.course_test.waitlist), 0)

        self.course_test.drop("STU00001")
        self.assertEqual(len(self.course_test.get_student_list()), 1)
        self.assertEqual(self.course_test.get_student_list()[0], self.student2)
        self.assertEqual(len(self.course_test.waitlist), 0)

        self.course_test.request_enroll(self.student1, enroll_date=datetime.date(2002, 12, 12))
        self.course_test.request_enroll(student3, enroll_date=datetime.date(2005, 12, 12))

        self.assertEqual(self.course_test.waitlist.peek(), student3)

        self.course_test.drop("STU00002", enroll_date_for_replacement=datetime.date(2010, 12, 13))
        self.assertEqual(self.course_test.get_student_list(), [self.student1, student3])

        self.assertEqual(
            self.course_test.get_student_enrollment_data("STU00003").enroll_date,
            datetime.date(2010, 12, 13)
        )

    def test_binary_search(self):
        self.assertEqual(self.course_test.sort_and_find_student_index("STU00005"), -1)
        self.assertEqual(self.course_test.sort_and_find_student_index("STU00001"), 0)

if __name__ == "__main__":
    unittest.main()




