import csv

class Person:
    def __init__(self,name,age,role,password):
        self.name = name
        self.age = age
        self.role = role
        self.password = password

    @classmethod # staff || students
    def all_people(cls, file):
        people =[]
        with open(f'./data/{file}.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                people.append(row)
        return people #returns list of dicts

