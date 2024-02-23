from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

second_app = Flask(__name__)

second_app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://franciscoavila@localhost/students'

db = SQLAlchemy(second_app)

class Students(db.Model): # table == Model
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(10))
    last_name = db.Column(db.String(10))
    age = db.Column(db.Integer)
    grade = db.Column(db.String(1))

# students = [
#     {'id': '1', 'first_name': 'John', 'last_name': 'Doe', 'age': '18', 'grade': 'A'},
#     {'id': '2', 'first_name': 'Jane', 'last_name': 'Smith', 'age': '19', 'grade': 'B'},
#     {'id': '3', 'first_name': 'Bob', 'last_name': 'Johnson', 'age': '20', 'grade': 'C'},
#     {'id': '4', 'first_name': 'Emily', 'last_name': 'Williams', 'age': '18', 'grade': 'A'},
#     {'id': '5', 'first_name': 'Michael', 'last_name': 'Brown', 'age': '19', 'grade': 'B'}
# ]

#GET- grabbing info
#PUT - updating info within db
#DELETE - deleting an entry within the db
#POST - creating an entry to the db
@second_app.route("/")
def index():
    return "Hello, World!"

@second_app.route('/api/v1/students/', methods=['GET'])
def get_all_students():
    # SELECT * FROM students;
    students = Students.query.all() # Students.objects.all()
    print(students)
    json_students = [{'id':stud.id, 'first_name':stud.first_name, 'last_name':stud.last_name, 'age':stud.age, 'grade':stud.grade} for stud in students]
    response = jsonify(json_students)
    return response

# print(get_all_students())

# if __name__ == '__main__':
second_app.run(debug=True)