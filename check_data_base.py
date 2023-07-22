from flask import Flask

import os

from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import Float

from sqlalchemy.sql import func

app = Flask(__name__)

##database definition using SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))

print(basedir,'basedir')

app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class gpt_data(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(100), nullable=True)
    password = db.Column(db.String(100), nullable=False)
    correct_questions = db.Column(db.Integer, nullable=False)
    time_replied = db.Column(db.String(100), nullable=False)
    num_questions = db.Column(db.Integer, nullable=False)
    correctness = db.Column(Float,nullable=False)
    correct_answers = db.Column(db.PickleType, nullable=True)
    time_taken = db.Column(db.PickleType, nullable=True)
    questions = db.Column(db.PickleType, nullable=True)

with app.app_context():
   ## responses here
   for i_data in range(0,5000):
       data=db.session.query(gpt_data).filter_by(id=i_data).first()
       #print(data)
       if not(data == None): 
           #print(data.correct_answers,data.questions,'data_answers')
           print(i_data,len(data.correct_answers),len(data.questions),'lens')


   data=db.session.query(gpt_data).filter_by(id=4283).first()
   print(data.questions,len(data.questions),'questions')
   print(data.correct_answers,len(data.correct_answers),'correct_answers')
   print(data.time_taken,len(data.time_taken),'time_taken')
   #db.session.query(gpt_data).filter_by(id=3533).delete()
   #db.session.commit()
   #data.questions.pop(14)
   #data.correct_answers.pop(14)
   #data.time_taken.pop(14)
   #db.session.query(gpt_data).filter(gpt_data.id == 4283).update({'num_questions':  9, 'correctness': float(7/9)*100})
   #db.session.query(gpt_data).filter(gpt_data.id == 4283).update({'questions': data.questions, 'time_taken': data.time_taken, 'correct_answers': data.correct_answers})
   #db.session.commit()
   ## questions here
   #for i_data in range(0,5000):
   #    data=db.session.query(gpt_data).filter_by(id=i_data).first()
   #    #print(data)
   #    if not(data == None): 
   #        print(data.questions,'data_questions')
   #db.session.query(gpt_data).filter(gpt_data.id == 3770).update({'username': 'naim', 'password': 'martin'})
