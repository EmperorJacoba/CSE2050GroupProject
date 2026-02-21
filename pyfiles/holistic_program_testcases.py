import random
import unittest
from student import Student, Grade
from course import Course
from university import University

def make_dummy_course(grade_list: list[Grade]) -> Course:
    course = Course("CSE 2050", 3)

    student1 = Student("STU94146", "Justin")
    student2 = Student("STU28734", "Justin2")
    student3 = Student("STU94122", "Justin3")
    student4 = Student("STU94322", "Justin4")

    student1.enroll(course, Grade(grade_list[0]))
    student2.enroll(course, Grade(grade_list[1]))
    student3.enroll(course, Grade(grade_list[2]))
    student4.enroll(course, Grade(grade_list[3]))

    return course

class TestCourse(unittest.TestCase):
    def test_init(self):
        course1 = Course("CSE 2050", 3, [])

        self.assertEqual(course1.course_code, "CSE 2050")
        self.assertEqual(course1.credits, 3)
        self.assertEqual(course1.students, [])

    def test_add_student(self):
        course1 = Course("CSE2050", 3, [])
        student1 = Student("STU74823", "Justin", {})

        course1.add_student(student1)
        self.assertEqual(course1.students, [student1])
        self.assertEqual(list(student1.courses.keys())[0], course1)

    def test_duplicate_add_student(self):
        course1 = Course("CSE2050", 3, [])
        student1 = Student("STU74823", "Justin", {})

        course1.add_student(student1)
        course1.add_student(student1)

        self.assertEqual(course1.students, [student1])

    def test_get_student_count(self):
        course1 = Course("CSE 2050", 3, [])

        random_num = random.randint(10, 99)
        for i in range(random_num):
            stu = Student(f"STU{random_num}000", f"Student{random_num}", {})
            grade_int = random.randrange(1, 100)
            course1.add_student(stu, Grade(grade_int))
            self.assertEqual(stu.courses, {course1: Grade(grade_int)})

        self.assertEqual(course1.get_student_count(), random_num)

    def test_get_mode(self):
        course = make_dummy_course([Grade("A"), Grade("A"), Grade("B"), Grade("C")])

        self.assertEqual(4.0, course.get_mode_grade_point())

    def test_get_median(self):
        course = make_dummy_course([Grade("A"), Grade("A"), Grade("B"), Grade("C")])

        self.assertEqual((4.0 + 3.0) / 2, course.get_median_grade_point())

        student5 = Student("STU12111", "Irrelevant")
        student5.enroll(course, Grade("D"))

        self.assertEqual(3.0, course.get_median_grade_point())

    def test_get_mean(self):
        course = make_dummy_course([Grade("A"), Grade("A"), Grade("B"), Grade("C")])

        self.assertEqual((4.0 + 4.0 + 3.0 + 2.0) / 4, course.get_mean_grade_point())

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
        self.assertEqual(student1.courses, {course1 : Grade("A")})
        self.assertEqual(course1.students, [student1])

    def test_calculate_gpa(self):
        course1 = Course("MATH 1132Q", 4, [])
        course2 = Course("PYSC 1000", 4, [])
        student1 = Student("STU94146", "Alex", {})

        self.assertEqual(student1.calculate_gpa(), 0)

        student1.enroll(course1, Grade("A"))
        student1.enroll(course2, Grade("B+"))
        expected_gpa = (8 * (4.0 + 3.3)) / 8 # expected equation outcome from GPA formula

        self.assertEqual(student1.calculate_gpa(), expected_gpa)

    def test_get_course_info(self):
        course1 = Course("MATH 1132Q", 4, [])
        student1 = Student("STU94146", "Alex", {})

        student1.enroll(course1, Grade("A"))
        self.assertEqual(student1.get_course_info().split("\n")[1], "Course: MATH 1132Q, Credits: 4, Grade: A")

class TestUniversity(unittest.TestCase):
    def test_init(self):
        university1 = University()

        self.assertEqual(university1.courses, {})
        self.assertEqual(university1.students, {})

        student1 = Student("STU94146","Justin")
        course1 = Course("Blah", 3)

        student_dict = {"STU94146": student1}
        course_dict = {"Blah": course1}
        university2 = University(student_dict, course_dict)

        self.assertEqual(course_dict, university2.courses)
        self.assertEqual(student_dict, university2.students)

    def test_add_course(self):
        university1 = University()
        course1 = university1.add_course("MATH 1132Q", 4)

        self.assertEqual(university1.courses, {"MATH 1132Q": course1})

    def test_add_duplicate_course(self):
        university1 = University()
        course1 = university1.add_course("MATH 1132Q", 4)
        university1.add_course("MATH 1132Q", 4)

        self.assertEqual(university1.courses, {"MATH 1132Q": course1})

    def test_add_student(self):
        university1 = University()

        student1 = university1.add_student("STU94146","Justin")

        self.assertEqual(university1.students, {"STU94146": student1})

    def test_add_student_duplicate(self):
        university1 = University()
        student1 = university1.add_student("STU94146","Justin")

        university1.add_student("STU94146","Justin")

        self.assertEqual(university1.students, {"STU94146": student1})

    def test_student_info(self):
        university1 = University()

        student1 = university1.add_student("STU94146","Justin")
        self.assertEqual(university1.get_student("STU94146"), student1)

    def test_student_missing_info(self):
        university1 = University()
        self.assertEqual(university1.get_student("STU94146"), None)

    def test_get_course(self):
        university1 = University()
        course1 = university1.add_course("MATH 1132Q", 4)
        self.assertEqual(university1.get_course("MATH 1132Q"), course1)

    def test_get_missing_course(self):
        university1 = University()
        self.assertEqual(university1.get_course("MATH 1132Q"), None)

    def test_get_median_gpa(self):
        university = University()
        student1 = university.add_student("STU94146","Justin")
        student2 = university.add_student("STU28734", "Justin2")
        student3 = university.add_student("STU94122","Justin3")

        course = Course("djd", 3, None)
        student1.enroll(course, Grade("A")) # 4.0
        student2.enroll(course, Grade("B")) # 3.0
        student3.enroll(course, Grade("F")) # 0.0

        # A, B, F => median (middle) is B
        self.assertEqual(3.0, university.get_median_gpa())

        student4 = university.add_student("STU94322","Justin4")
        student4.enroll(course, Grade("C")) # 2.0

        # A, B, C, F => by grade point, B + C = 2.0 + 3.0 / 2 = 5 / 2 = 2.5
        self.assertEqual((2.0 + 3.0) / 2, university.get_median_gpa())

    def test_get_mean_gpa(self):
        university = University()
        student1 = university.add_student("STU94146","Justin")
        student2 = university.add_student("STU28734", "Justin2")
        student3 = university.add_student("STU94122","Justin3")
        student4 = university.add_student("STU94322","Justin4")

        course = Course("djd", 3, None)
        student1.enroll(course, Grade("A")) # 4.0
        student2.enroll(course, Grade("B")) # 3.0
        student3.enroll(course, Grade("D")) # 1.0
        student4.enroll(course, Grade("F")) # 0.0

        # 8.0 / 4 = 2
        self.assertEqual(8.0 / 4, university.get_mean_gpa())


if __name__ == '__main__':
    unittest.main()