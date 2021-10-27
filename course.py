from professor import Professor
from enroll import Enroll

class Course:
    def __init__(self, name, code, max, min, professor):
        self.name = name
        self.code = code
        self.max = max
        self.min = min
        self.professors = []
        self.enrollments = []

        if isinstance(professor,Professor):
            self.professores.append(professor)
        elif isinstance(professor,list):
            for entry in professor:
                if not isinstance(entry, Professor):
                    raise KeyError("Invalid Professor...")

            self.professores = professor
        else:
            raise KeyError("Invalid professor..")

    def add_professor(self, professor):
        if not isinstance(professor,Professor):
            raise KeyError("Invalid professor...")

        self.professors.append(professor)

    def add_enrollment(self, enroll):
        if not isinstance(enroll, Enroll):
            raise KeyError("Invalid Enroll...")

        if len() == self.max:
            raise KeyError("Cannot enroll, course if full...")

        self.enrollments.append(enroll)

    def is_cancelled(self):
        return len(self.enrollments) < self.min