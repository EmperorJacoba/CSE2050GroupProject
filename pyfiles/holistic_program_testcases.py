import random
import unittest
from student import Student, Grade
from course import Course
from university import University

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

class TestCourse(unittest.TestCase):
    def test_init(self):
        """
        Test Course object initialization to PDF specifications

        Created by Justin Elak
        """
        course1 = Course("CSE 2050", 3, [])

        self.assertEqual(course1.course_code, "CSE 2050")
        self.assertEqual(course1.credits, 3)
        self.assertEqual(course1.enrollments, [])

    def test_add_student(self):
        """
        Test Course.add_student() to PDF specifications

        Created by Justin Elak
        """
        course1 = Course("CSE2050", 3, [])
        student1 = Student("STU74823", "Justin", {})

        course1.add_student(student1)
        self.assertEqual(course1.enrollments, [student1])
        self.assertEqual(list(student1.courses.keys())[0], course1)

    def test_duplicate_add_student(self):
        """
        Test Course.add_student() to ensure that adding duplicate student objects/ids has no effect (only one student remains)

        Created by Jacob Russell
        """
        course1 = Course("CSE2050", 3, [])
        student1 = Student("STU74823", "Justin", {})

        course1.add_student(student1)
        course1.add_student(student1)

        self.assertEqual(course1.enrollments, [student1])

    def test_get_student_count(self):
        """
        Test Course.get_student_count() to check it correctly returns the number of added students.

        Created by Jacob Russell
        """
        course1 = Course("CSE 2050", 3, [])

        random_num = random.randint(10, 99)
        for i in range(random_num):
            stu = Student(f"STU{random_num}000", f"Student{random_num}", {})
            grade_int = random.randrange(1, 100)
            course1.add_student(stu, Grade(grade_int))
            self.assertEqual(stu.courses, {course1: Grade(grade_int)})

        self.assertEqual(course1.get_student_count(), random_num)

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

# Make sure to add tests that check validation
# e.g. pass in invalid student IDs, invalid grades, and make sure they bounce
# Also check to make sure duplicate entries are rejected/show no change
class TestStudent(unittest.TestCase):
    def test_init(self):
        """
        Test object initialization of a new Student object according to PDF specifications.

        Created by Justin Elak
        """
        student1 = Student("STU94146", "Alex", {})

        self.assertEqual(student1.student_id,"STU94146")
        self.assertEqual(student1.name, "Alex")
        self.assertEqual(student1.courses, {})

    def test_enroll(self):
        """
        Test Student.enroll() according to PDF specifications

        Created by Justin Elak
        """
        course1 = Course("MATH 1132Q", 4, [])
        student1 = Student("STU94146", "Alex", {})

        student1.enroll(course1, Grade("A"))
        self.assertEqual(student1.courses, {course1 : Grade("A")})
        self.assertEqual(course1.enrollments, [student1])

    def test_calculate_gpa(self):
        """
        Test Student.calculate_gpa() to ensure it properly calculates the GPA of a student.

        Created by Jacob Russell
        """
        course1 = Course("MATH 1132Q", 4, [])
        course2 = Course("PYSC 1000", 4, [])
        student1 = Student("STU94146", "Alex", {})

        self.assertEqual(student1.calculate_gpa(), 0)

        student1.enroll(course1, Grade("A"))
        student1.enroll(course2, Grade("B+"))

        expected_gpa = (4*4 + 4*3.3) / 8

        self.assertEqual(student1.calculate_gpa(), expected_gpa)

    def test_get_course_info(self):
        """
        Test Student.get_course_info() to ensure it properly prints enrolled course information.

        Created by Justin Elak
        """
        course1 = Course("MATH 1132Q", 4, [])
        student1 = Student("STU94146", "Alex", {})

        student1.enroll(course1, Grade("A"))
        self.assertEqual(student1.get_course_info().split("\n")[1], "Course: MATH 1132Q, Credits: 4, Grade: A")

class TestUniversity(unittest.TestCase):
    def test_init(self):
        """
        Test object initialization of a new University object to ensure it matches PDF specifications

        Created by Jacob Russell
        """
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
        """
        Test University.add_course() to ensure university course roster reflects added courses

        Created by Jacob Russell
        """
        university1 = University()
        course1 = university1.add_course("MATH 1132Q", 4)

        self.assertEqual(university1.courses, {"MATH 1132Q": course1})

    def test_add_duplicate_course(self):
        """
        Test University.add_course() to ensure adding duplicate course objects has no effect

        Created by Jacob Russell
        """
        university1 = University()
        course1 = university1.add_course("MATH 1132Q", 4)
        university1.add_course("MATH 1132Q", 4)

        self.assertEqual(university1.courses, {"MATH 1132Q": course1})

    def test_add_student(self):
        """
        Test University.add_student() to ensure adding a student to a university is properly reflected in the University's
        student info

        Created by Jacob Russell
        """
        university1 = University()

        student1 = university1.add_student("STU94146","Justin")

        self.assertEqual(university1.students, {"STU94146": student1})

    def test_add_student_duplicate(self):
        """
        Test University.add_student() to ensure adding duplicate students has no effect on the University student roster

        Created by Jacob Russell
        """
        university1 = University()
        student1 = university1.add_student("STU94146","Justin")

        university1.add_student("STU94146","Justin")

        self.assertEqual(university1.students, {"STU94146": student1})

    def test_student_info(self):
        """
        Test University.get_student() to check it returns the correct student object for a given student ID

        Created by Jacob Russell
        """
        university1 = University()

        student1 = university1.add_student("STU94146","Justin")
        self.assertEqual(university1.get_student("STU94146"), student1)

    def test_student_missing_info(self):
        """
        Test University.get_student() to ensure it returns None upon requesting a nonexistent student

        Created by Jacob Russell
        """
        university1 = University()
        self.assertEqual(university1.get_student("STU94146"), None)

    def test_get_course(self):
        """
        Test University.get_course() to ensure it returns the correct course object associated with a course ID

        Created by Jacob Russell
        """
        university1 = University()
        course1 = university1.add_course("MATH 1132Q", 4)
        self.assertEqual(university1.get_course("MATH 1132Q"), course1)

    def test_get_missing_course(self):
        """
        Test University.get_course() to ensure it returns None when requesting a nonexistent course

        Created by Jacob Russell
        """
        university1 = University()
        self.assertEqual(university1.get_course("MATH 1132Q"), None)

    def test_get_median_gpa(self):
        """
        Test University.get_median_gpa() to ensure it returns the correct calculation for median GPA based on added students.

        Created by Jacob Russell
        """
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
        """
        Test University.get_mean_gpa() to ensure it properly calculates mean GPA based on added students

        Created by Jacob Russell
        """
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