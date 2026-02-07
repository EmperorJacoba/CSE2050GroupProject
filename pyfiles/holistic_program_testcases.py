import unittest
from student_class import Student
from course import Course
from university import University


class TestCourse(unittest.TestCase):
    def test_init(self):
        course1 = Course("CSE2050", 3,[])
        self.assertEqual(course1.course_code, "CSE2050")
        self.assertEqual(course1.credits, 3)
        self.assertEqual(course1.students, [])

    def test_add_student(self):
        course1 = Course("CSE2050", 3,[])
        student1 = Student("STU74823", "Justin", {})
        course1.add_student(student1)
        self.assertEqual(course1.students, [student1])


if __name__ == '__main__':
    unittest.main()
