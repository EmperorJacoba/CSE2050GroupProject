import unittest
from hash import HashMap
from course import Course
from student import Student
from student import Grade
import datetime

class TestHashMap(unittest.TestCase):
    def setUp(self):
        """
        Setup hashmap with length 2 for tests

        Created by Justin Elak
        """
        self.hm = HashMap()

    def test_set(self):
        """
        Test the set method, should allow all immutable data types to be used as a key

        Created by Justin Elak
        """
        self.hm[1] = "Hi"
        self.hm["foo"] = 10
        self.hm[(1,2)] = 2

    def test_get(self):
        """
        Make sure the get method returns the correct data

        Created by Justin Elak
        """
        self.hm[1] = "buzz"
        self.hm["foo"] = 10
        self.hm[(10,20,30)] = True

        self.assertEqual(self.hm[1], "buzz")
        self.assertEqual(self.hm["foo"], 10)
        self.assertEqual(self.hm[(10,20,30)], True)
        with self.assertRaises(KeyError):
            _ = self.hm["bar"]

    def test_collision_handling(self):
        """
        Makes sure collisions are handled correctly and saves data correctly when values are the same

        Created by Justin Elak
        """
        #Both key%4 = 0
        self.hm = HashMap(size=4)
        self.hm[0] = "foo"
        self.hm[4] = "bar"

        self.assertEqual(self.hm[0], "foo")
        self.assertEqual(self.hm[4], "bar")

    def test_rehashing(self):
        """
        Checks if data is stored correctly after a rehash is done

        Created by Justin Elak
        """
        self.hm = HashMap(size=4)
        self.hm[0] = "foo"
        self.hm[4] = "bar"
        self.hm[2] = "buzz"
        #Should rehash after 4th
        self.hm[6] = "bat"

        #Checks if all data was correctly rehashed
        self.assertEqual(self.hm[0], "foo")
        self.assertEqual(self.hm[4], "bar")
        self.assertEqual(self.hm[2], "buzz")
        self.assertEqual(self.hm[6], "bat")

    def test_len(self):
        """
        See if hashmap length is correctly updated when keys are added and stays the same when a value is changed

        Created by Justin Elak
        """

        self.assertEqual(0, len(self.hm))
        self.hm[1] = "foo"
        self.assertEqual(1, len(self.hm))
        self.hm[2] = "buzz"
        self.assertEqual(2, len(self.hm))
        self.hm[2] = "bar"
        self.assertEqual(2, len(self.hm))

class TestEnrollments(unittest.TestCase):
    def test_check_for_prerequisites(self):
        Course.prerequisite = HashMap(size=1)
        Course.prerequisite["TEST2000"] = "TEST1000"

        course1 = Course("TEST1000", 3)
        course2 = Course("TEST2000", 3)

        stu = Student("STU81992", "John Teston")

        with self.assertRaises(PermissionError):
            stu.enroll(course2, Grade("A"))

        stu.enroll(course1, Grade("A"))
        stu.enroll(course2, Grade("A"))

        self.assertEqual(course1 in stu.courses, True)
        self.assertEqual(course2 in stu.courses, True)
        self.assertEqual(stu in course1.get_student_list(), True)
        self.assertEqual(stu in course2.get_student_list(), True)

class TestSortingAlgorithms(unittest.TestCase):
    def setUp(self):
        """
        Set up a course and three students for milestone 3 functionality testing.

        Created by Jacob Russell
        """
        self.capacity = 3
        self.credits = 3
        self.course_test = Course("TEST1100", self.credits, capacity=self.capacity)

        # Sorting orders - different orders for each field to ensure each sorting category works
        # ID: 1,2,3
        # Name: 2,3,1
        # Date: 3,2,1
        self.student1 = Student("STU00001", "Clam")
        self.student2 = Student("STU00002", "Albert")
        self.student3 = Student("STU00003", "Brainiac")

        self.course_test.request_enroll(self.student1, enroll_date=datetime.date(2002, 1, 1))
        self.course_test.request_enroll(self.student2, enroll_date=datetime.date(2001, 1, 1))
        self.course_test.request_enroll(self.student3, enroll_date=datetime.date(2000, 1, 1))

    def test_merge_sort(self):
        self.course_test.sort_enrolled("id", "merge")
        self.assertEqual(self.course_test.enrolled_sorted_by, "id")
        self.assertEqual(self.course_test.get_student_list(), [self.student1, self.student2, self.student3])

        self.course_test.sort_enrolled("name", "merge")
        self.assertEqual(self.course_test.enrolled_sorted_by, "name")
        self.assertEqual(self.course_test.get_student_list(), [self.student2, self.student3, self.student1])

        self.course_test.sort_enrolled("date", "merge")
        self.assertEqual(self.course_test.enrolled_sorted_by, "date")
        self.assertEqual(self.course_test.get_student_list(), [self.student3, self.student2, self.student1])

    def test_quick_sort(self):
        self.course_test.sort_enrolled("id", "quick")
        self.assertEqual(self.course_test.enrolled_sorted_by, "id")
        self.assertEqual(self.course_test.get_student_list(), [self.student1, self.student2, self.student3])

        self.course_test.sort_enrolled("name", "quick")
        self.assertEqual(self.course_test.enrolled_sorted_by, "name")
        self.assertEqual(self.course_test.get_student_list(), [self.student2, self.student3, self.student1])

        self.course_test.sort_enrolled("date", "quick")
        self.assertEqual(self.course_test.enrolled_sorted_by, "date")
        self.assertEqual(self.course_test.get_student_list(), [self.student3, self.student2, self.student1])

if __name__ == "__main__":
    unittest.main()