import datetime

class EnrollmentRecord:
    def __init__(self, student: "Student", enroll_date: datetime.date = None):
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
                raise ValueError("Invalid sorting method")

