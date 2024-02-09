from classes.person import Person

class Student(Person):

    def __init__(self, name,age,role,school_id,password):
        super().__init__(name,age,role,password)
        self.school_id = school_id

    @classmethod
    def all_students(cls):
        student_data = Person.all_people("students") #returns a list of dict
        students = [cls(**stud) for stud in student_data] #iter through list of stud_dict to create Student instances
        # for stud in student_data:
        #     students.append(csl(**stud))
        return students

    def __repr__(self):
        return self.name




