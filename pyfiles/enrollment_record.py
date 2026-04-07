import datetime
from student import Student

class EnrollmentRecord:
    def __init__(self, student: Student, enroll_date: datetime.date = None):
        self.student = student

        if not enroll_date:
            self.enroll_date = datetime.date.today()
        else:
            self.enroll_date = enroll_date

    def get_property(self, type: str):
        match type:
            case "name":
                return self.student.name
            case "id":
                return self.student.student_id
            case "date":
                return self.enroll_date
            case _:
                raise ValueError(f"Invalid sorting method, \"{type}\" is not a supported property.")

    def __str__(self):
        return f"{self.student}, enroll time: {self.enroll_date}"

