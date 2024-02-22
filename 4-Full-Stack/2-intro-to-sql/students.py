import csv


class Student:
    def __init__(self, id, first_name, last_name, age, grade):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"ID: {self.id} \nName: {self.first_name} \n{self.last_name} \nAge: {self.age} \nGrade: {self.grade}"

    @classmethod  # ./resources/data.csv
    def read_student_data(cls, file_path):
        student_lst = []
        with open(file_path, mode="r", newline="") as csv_file:
            reader = csv.DictReader(csv_file)
            # [{},{},{},{}]
            for row in reader:
                student = Student(**row)
                student_lst.append(student)
        return student_lst
    
    @classmethod
    def write_student_data(cls, file_path, students):
        with open(file_path, mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['id','first_name','last_name','age','grade'])
            for stud in students:
                writer.writerow([stud.id, stud.first_name, stud.last_name, stud.age, stud.grade])



def main():
    file_path = "./resources/data.csv"
    results_path = "./resources/results.csv"
    students = Student.read_student_data(file_path)
    print(students)
    while True:
        print(
            """
Student Management System
1. View Students
2. Add Student
3. Delete a Student
4. Exit
              """
        )
        choice = input("Enter your choice:  ")
        if choice == '1':
            for stud in students:
                print(stud)
        elif choice == '2':
            new_student = {
                "id" : input("New student id:   "),
                "first_name" : input("New student first name:   "),
                "last_name" : input("New student last name:   "),
                "age" : input("New student age:   "),
                "grade" : input("New student grade:   "),
            }
            students.append(Student(**new_student))
            print("New student was added!")
        elif choice == '3':
            student_to_delete = input("ID of student to be deleted: ")
            new_lst_of_stud = []
            for stud in students:
                if stud.id != student_to_delete:
                    new_lst_of_stud.append(stud)
            students = new_lst_of_stud
            print("Student deleted successfully.")
        elif choice == '4':
            Student.write_student_data(results_path, students)
            print("Goodbye")
            break
        else:
            print("Improper input!")

main()