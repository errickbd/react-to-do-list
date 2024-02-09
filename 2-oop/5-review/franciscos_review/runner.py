from classes.school import School

menu = """
Ridgemont High Student Interface 
--------------------------------
Welcome, Richard. Your access level is Principal
    What would you like to do?
    Options:
    1 List All Students
    2 View Individual Student <student_id>
    3 Add a Student
    4 Remove a Student <student_id>
    5 Quit
"""

def run_the_runner():
    new_school = School("Ridgemont")
    while True:
        choice = input(menu)
        if choice == "1":
            print(new_school.students)
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            break
        else:
            run_the_runner()

run_the_runner()