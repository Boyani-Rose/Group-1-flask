from flask_migrate import Migrate
from flask import Flask, request, make_response, jsonify
from models import db, Student, Mentor, Reward, Cohort


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def index():
    return '<h1>Welcome to the homepage!</h1>'

@app.route('/students')
def get_students():
    students_list=[]
    students=Student.query.all()
    for student in students:
        students_list.append(student.to_dict())
    return make_response(students_list, 200)

@app.route('/students/<int:id>')
def get_students_byId(id):
    
    student=Student.query.get(id)
    
    return make_response(student.to_dict(), 200)

@app.route('/mentors')
def get_mentors():
    mentors_list=[]
    mentors=Mentor.query.all()
    for mentors in mentors:
        mentors_list.append(mentors.to_dict())
    return make_response(mentors_list, 200)

@app.route('/mentors/<int:id>')
def get_mentors_byId(id):
    
    mentors=Mentor.query.get(id)
    
    return make_response(mentors.to_dict(), 200)















if __name__ == '__main__':
    app.run(port=5555, debug=True)

