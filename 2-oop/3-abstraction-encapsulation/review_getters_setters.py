class Student:
    """
    - name: str student name
    - age: int student age
    - grade: int student grade
    """
    def __init__(self, name, age, grade):
        print("This is the constructor method for the student class")

        self.name = name
        self.set_grade = grade

    @property
    def get_age(self):
        return self._age

    @property
    def get_grade(self):
        if self._grade == None:
            return "NO GRADE"
        else:
            grade_num = str(self._grade)
            return f"{grade_num}th" #TODO: Handle "2nd", "1st", "12th", etc

    @get_grade.setter
    def set_grade(self, new_grade):
        if new_grade == 0:
            print("Must enter valid grade")
            self._grade = None
        else:
            self._grade = new_grade

alice = Student("Alice", 18, 0)
bob = Student("Bob", 10, 2)

print(alice.name)
print(bob.name)

print(bob.get_age)
print(alice.get_age)

print(alice.get_grade)
print(bob.get_grade)

alice.set_grade = 14
print(alice.get_age)