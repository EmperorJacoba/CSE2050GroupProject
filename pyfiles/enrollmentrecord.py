import datetime

class EnrollmentRecord:
    def __init__(self, student: "Student", enroll_date: datetime.date = None):
        self.student = student

        if not enroll_date:
            self.enroll_date = datetime.date.today()
        else:
            self.enroll_date = enroll_date

