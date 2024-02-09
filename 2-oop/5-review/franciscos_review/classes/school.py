from classes.students import Student

class School:

    def __init__(self, name):
        self.name = name
        self.students = Student.all_students() #[Student(1), Student(2),...]
        self.staff = []


