import unittest
from student import Student, Grade
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

    def test_duplicate_add_student(self):
        course1 = Course("CSE2 050", 3, [])
        student1 = Student("STU74823", "Justin", {})
        course1.add_student(student1)
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
        student1.enroll(course1, Grade("A"))
        self.assertEqual(student1.courses, {course1:"A"})

    def test_calculate_gpa(self):
        course1 = Course("MATH 1132Q", 4, [])
        student1 = Student("STU94146", "Alex", {})
        student1.enroll(course1, Grade("A"))
        self.assertEqual(student1.calculate_gpa(), 4)

    def test_get_course_info(self):
        course1 = Course("MATH 1132Q", 4, [])
        student1 = Student("STU94146", "Alex", {})
        student1.enroll(course1, Grade("A"))
        self.assertEqual(student1.get_course_info, "Course: MATH 1132Q, Credits: 4, Grade: A")

class TestUniversity(unittest.TestCase):
    def test_init(self):
        university1 = University({},{})
        self.assertEqual(university1.courses, {})
        self.assertEqual(university1.students, {})

    def test_add_course(self):
        university1 = University({},{})
        course1 = university1.add_course("MATH 1132Q", 4)
        self.assertEqual(university1.courses, {"MATH 1132Q": course1})

    def test_add_duplicate_course(self):
        university1 = University({},{})
        course1 = university1.add_course("MATH 1132Q", 4)
        university1.add_course("MATH 1132Q", 4)
        self.assertEqual(university1.courses, {"MATH 1132Q": course1})

    def test_add_student(self):
        university1 = University({},{})
        course1 = university1.add_course("MATH 1132Q", 4)
        university1.add_course("MATH 1132Q", 4)
        student1 = university1.add_student("STU94146","Justin")
        self.assertEqual(university1.students, {"STU94146", student1})

    def test_add_student_duplicate(self):
        university1 = University({},{})
        course1 = university1.add_course("MATH 1132Q", 4)
        university1.add_course("MATH 1132Q", 4)
        student1 = university1.add_student("STU94146","Justin")
        university1.add_student("STU94146","Justin")
        self.assertEqual(university1.students, {"STU94146", student1})

    def test_student_info(self):
        university1 = University({},{})
        course1 = university1.add_course("MATH 1132Q", 4)
        university1.add_course("MATH 1132Q", 4)
        student1 = university1.add_student("STU94146","Justin")
        self.assertEqual(university1.get_student("STU94146"), student1)

    def test_student_missing_info(self):
        university1 = University({},{})
        course1 = university1.add_course("MATH 1132Q", 4)
        university1.add_course("MATH 1132Q", 4)
        self.assertEqual(university1.get_student("STU94146"), None)

    def test_get_course(self):
        university1 = University({},{})
        course1 = university1.add_course("MATH 1132Q", 4)
        university1.add_course("MATH 1132Q", 4)
        self.assertEqual(university1.get_course("MATH 1132Q"), course1)

    def test_get_missing_course(self):
        university1 = University({},{})
        course1 = university1.add_course("MATH 1132Q", 4)
        university1.add_course("MATH 1132Q", 4)
        self.assertEqual(university1.get_course("MATH 1132Q"), None)

if __name__ == '__main__':
    unittest.main()