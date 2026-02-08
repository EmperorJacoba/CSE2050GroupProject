import unittest
from student import Student
from course import Course
from university import University


class TestCourse(unittest.TestCase):
    def test_init(self):
        course1 = Course("CSE 2050", 3, [])
        self.assertEqual(course1.course_code, "CSE 2050")
        self.assertEqual(course1.credits, 3)
        self.assertEqual(course1.students, [])

    def test_add_student(self):
        course1 = Course("CSE2 050", 3, [])
        student1 = Student("STU74823", "Justin", {})
        course1.add_student(student1)
        self.assertEqual(course1.students, [student1])

    def test_get_student_count(self):
        course1 = Course("CSE 2050", 3, [])
        student1 = Student("STU74823", "Justin", {})
        course1.add_student(student1)
        self.assertEqual(course1.get_student_count(),1)

# Make sure to add tests that check validation
# e.g. pass in invalid student IDs, invalid grades, and make sure they bounce
# Also check to make sure duplicate entries are rejected/show no change
class TestStudent(unittest.TestCase):
    def test_init(self):
        student1 = Student("STU94146", "Alex", {})
        self.assertEqual(student1.student_id,"STU94146")
        self.assertEqual(student1.name, "Alex")
        self.assertEqual(student1.courses, {})

    def test_enroll(self):
        course1 = Course("MATH 1132Q", 4, [])
        student1 = Student("STU94146", "Alex", {})
        student1.enroll(course1, "A")
        self.assertEqual(student1.courses, {course1:"A"})

    def test_get_course_info(self):
        course1 = Course("MATH 1132Q", 4, [])
        student1 = Student("STU94146", "Alex", {})
        student1.enroll(course1, "A")
        self.assertEqual(student1.get_course_info, "Course: MATH 1132Q, Credits: 4, Grade: A")


class TestUniversity(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()
