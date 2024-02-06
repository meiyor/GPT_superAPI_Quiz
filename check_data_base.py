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
           print(i_data,len(data.correct_answers),len(data.questions),len(data.time_taken),'lens')
           data=db.session.query(gpt_data).filter_by(id=i_data).first()
           for iindex in range(0,len(data.correct_answers)):
               data_split=data.correct_answers[iindex].split(':')
               if not (len(data_split)==3) or len(data_split[2])==0 or data_split[2]==' ' or data_split=='\n':
                  print('review',i_data)
                  break
           #if not(len(data.questions)==len(data.time_taken)):
           #   data.time_taken=data.time_taken[len(data.time_taken)-len(data.questions):len(data.time_taken)+1]
           #   db.session.query(gpt_data).filter(gpt_data.id == i_data).update({'time_taken': data.time_taken})
           #   db.session.commit()

   data=db.session.query(gpt_data).filter_by(id=2815).first()
   print(data.questions,len(data.questions),'questions')
   print(data.correct_answers,len(data.correct_answers),'correct_answers')
   print(data.time_taken,len(data.time_taken),'time_taken')
   #for i_data in range(0,len(data.questions)):
   #    data.questions[i_data]=data.questions[i_data].replace('NEW /difficult random question:','')
   #    data.questions[i_data]=data.questions[i_data].replace('NEW/difficult random question:','')
   #db.session.query(gpt_data).filter_by(id=4500).delete()
   #db.session.commit()
   #data.time_taken=[5.683459281921387, 9.632741212844849, 10.04816484451294, 12.584947109222412, 87.63861966133118, 15.637583255767822, 33.524253129959106, 8.863523721694946, 23.089061737060547, 25.995476722717285, 42.53087067604065, 33.473714113235474, 85.02646040916443, 10.15870976448059, 9.169517040252686, 20.679317474365234, 16.581291913986206, 71.13005375862122]
   #data.time_taken.pop(27)
   #print(data.correct_answers[8])
   #data.correct_answers[1]='0=> reply: E correct answer: 5,555°C'
   #data.correct_answers[15]='0=> reply: C correct answer: A Osmium '
   #data.correct_answers[13]='1=> reply: B correct answer:  b) Md'
   #data.questions.pop(19)
   #data.questions[3]='  In the field of mathematics, which conjecture remained unsolved for over 300 years until it was finally proven in 2002?  A) Goldbach Conjecture B) Riemann Hypothesis C) Poincaré Conjecture D) Collatz Conjecture     '
   #data.questions[8]='What is the capital city of France?  A) London B) Rome C) Paris'
   #db.session.query(gpt_data).filter(gpt_data.id == 1424).update({'questions': data.questions})
   #data.time_taken.pop(11)
   #data.correct_answers[8]='1=> reply: C correct answer:  c) Canberra'
   #data.time_taken=data.time_taken[len(data.time_taken)-25:len(data.time_taken)+1]
   #print(data.time_taken,len(data.time_taken),'len')
   #db.session.query(gpt_data).filter(gpt_data.id == 4028).update({'questions': data.questions})
   #data.correct_answers.pop(9)
   #data.time_taken.pop(9)
   #db.session.query(gpt_data).filter(gpt_data.id == 2813).update({'correct_questions': 13, 'num_questions':  15, 'correctness': float(13/15)*100, 'correct_answers': data.correct_answers})
   #db.session.query(gpt_data).filter(gpt_data.id == 802).update({'correct_answers': data.correct_answers}) ##'time_taken': data.time_taken})
   #db.session.commit()
   ## questions here
   #for i_data in range(0,5000):
   #    data=db.session.query(gpt_data).filter_by(id=i_data).first()
   #    #print(data)
   #    if not(data == None): 
   #        print(data.questions,'data_questions')
   #db.session.query(gpt_data).filter(gpt_data.id == 3770).update({'username': 'naim', 'password': 'martin'})
