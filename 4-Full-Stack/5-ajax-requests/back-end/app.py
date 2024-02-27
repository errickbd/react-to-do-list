from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

second_app = Flask(__name__)
CORS(second_app)

second_app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg://franciscoavila@localhost/students'

db = SQLAlchemy(second_app)

class Students(db.Model): # table == Model
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(10))
    last_name = db.Column(db.String(10))
    age = db.Column(db.Integer)
    grade = db.Column(db.String(1))

#GET- grabbing info
#PUT - updating info within db
#DELETE - deleting an entry within the db
#POST - creating an entry to the db
@second_app.route("/")
def index():
    return "Hello, World!"

# http://127.0.0.1:5500/api/v1/students/
@second_app.route('/api/v1/students/', methods=['GET'])
def get_all_students():
    # SELECT * FROM students;
    students = Students.query.all() # Students.objects.all()
    print(students)
    json_students = [{'id':stud.id, 'first_name':stud.first_name, 'last_name':stud.last_name, 'age':stud.age, 'grade':stud.grade} for stud in students]
    response = jsonify(json_students)
    print(response)
    return response

# print(get_all_students())

# if __name__ == '__main__':
second_app.run(debug=True)