from flask import Flask, render_template, request, jsonify

## keep this  commented and run ngrok from a separate terminal it generates multiple errors running it inside the code
#from flask_ngrok import  run_with_ngrok

import subprocess

import os

import webbrowser

import random

from flask_cors import CORS

from question_generator_superAPI import get_response, get_Quiz

from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import Float

from sqlalchemy.sql import func

#from flask import session

#from pyngrok import conf

#global string_quiz do it inside each Flask function
# create always a new connection with ngrok

subprocess.call("curl -s localhost:4040/api/tunnels | jq -r '.tunnels[0].public_url' > static/endpoint.txt",shell=True)
subprocess.call("chmod 777 static/endpoint.txt",shell=True)
subprocess.call("chown jmm:jmm static/endpoint.txt",shell=True)

fire_path="/usr/bin/firefox"
webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(fire_path), preferred=0)

browser= webbrowser.get('firefox')

string_quiz = []
string_prev = []
count_questions = 0
correct_count=0
prev_questions = []
username = []
password = []

number_questions=random.randint(3,15)

app = Flask(__name__)

##database definition using SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))

print(basedir,'basedir')

app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

## define the table of the database
class gpt_data(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(100), nullable=True)
    password = db.Column(db.String(100), nullable=False)
    correct_questions = db.Column(db.Integer, nullable=False)
    num_questions = db.Column(db.Integer, nullable=False)
    correctness = db.Column(Float,nullable=False)
    questions = db.Column(db.PickleType, nullable=True)
    
    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return f'<GPT {self.firstname}>'

app.secret_key = 'secret_key'
CORS(app)

#run_with_ngrok(app)
## define local variables in Flask

@app.get("/")
def index_get():
   return render_template("base.html")
#@app.route('/')
#def home():
#   return render_template("base.html")
@app.post("/adduser")
def adduser():
    ack=1
    global username
    global password
    userpass =  request.get_json()
    print(userpass)
    username=userpass.get("user")
    password=userpass.get("pass")
    return jsonify(ack)

@app.post("/ini")
def ini():
    global string_quiz
    global string_prev
    global count_questions
    global correct_count
    global number_questions
    global prev_questions

    prev_questions = []
    number_questions=random.randint(3,15)
    #text =  request.get_json().get("message")
    #string_quiz=get_Quiz()
    # TODO: check if text is valid
    count_questions = 0
    correct_count = 0
    string_quiz=get_Quiz(0,prev_questions)
    string_prev=string_quiz[1]
    prev_questions.append(string_quiz[0])
    length_quiz=number_questions
    message =  {"answer": f"the quiz is ready! Want to start the {length_quiz} questions?"}
    print(message,'message')
    return jsonify(message)

@app.post("/predict")
def predict():
    global string_quiz
    global string_prev
    global count_questions
    global correct_count
    global number_questions
    global prev_questions
    global username
    global password
    ## initialize correctness in 0
    correctness =0

    text =  request.get_json().get("message")
    #string_quiz=get_Quiz()
    # TODO: check if text is valid
    if not(text.lower() == 'yes') and not(text.lower() == 'y'):
       count_questions=count_questions+1
    
    if (text.lower() == 'yes' or text.lower() == 'y') and count_questions>=number_questions:
          ##database update
          GPT = gpt_data(id=random.randint(0,1000),username=username,password=password,correct_questions=correct_count,num_questions=number_questions,correctness=(correct_count/number_questions)*100,questions=string_prev)
          db.session.add(GPT)
          db.session.commit()
          number_questions=random.randint(3,15)
          #prev_questions = []
          count_questions = 0
          correct_count = 0
          string_prev=string_quiz[1]
          length_quiz=number_questions
          message =  {"answer": f"Quiz is ready! Want to start the {length_quiz} questions?"}
          print(message,'message')
          return jsonify(message)

    ##evaluate correctness before to process more difficult questions before
    if text[0].lower() == string_prev[2].lower() or text.lower() in string_prev.lower(): ## evaluate correctness of the question before calling the request
         correctness=1
    else:
         correctness=0
   
    string_quiz=get_Quiz(correctness,prev_questions)
    while len(string_quiz)==1:
       string_quiz=get_Quiz(correctness,prev_questions)
    
    prev_questions.append(string_quiz[0])

    response, correct_count = get_response(text,string_quiz,count_questions,correct_count,number_questions,string_prev)
    string_prev = string_quiz[1]
    print(string_prev,'message','count',count_questions)
    
    ##add the number of questions answered correctly
    if count_questions > 0 and not(text.lower() == 'yes') and not(text.lower() == 'y') and not(text.lower() == 'no') and not(text.lower() == 'n'):
        response = response + f"\n You have anwered {correct_count}/{number_questions} questions correctly!"
    
    response = response.replace('\n', '<br/>') ## subtitute \n by <br\> for the html reading in the chat widget
    message =  {"answer": response}
    print(message,text,'message')
    return jsonify(message)

if __name__ == "__main__":
   ## uncomment this only if you want to use a second window in your web browser in this case firefox
   #if cf_port is None:
   #		app.run(host='127.0.0.1', port=5000, debug=True)
   #else:
   #		app.run(host='127.0.0.1', port=int(cf_port), debug=True)
   #string_quiz=get_Quiz()
   #url = 'http://127.0.0.1:5000'
   #browser.open(url)
   #url = 'http://127.0.0.1:5000'
   #browser.open_new(url)
   app.run() #use_reloader=False)
