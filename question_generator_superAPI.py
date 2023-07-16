import requests
import random
import time
string_quiz=[]
indices=[]

def get_Quiz(correctness,prev_questions):
  #resp = "Wait until the Quiz is loaded..\n"
  prev_question_string = ""
  temperature=random.uniform(0,1)
  if temperature<=0.5:
     temperature=temperature+0.85
  if temperature > 1:
     temperature=1
  ## request connection with SuperAPI interface 
  url = 'https://superapi.ai/v2/juan-manuelmayor-torres/chat-quiz'
  headers = {
    'accept': 'text/plain',
    'Authorization': 'Bearer r:4449c8f1b107d6a6aea6c017ec071d9c',
    'Content-Type': 'text/plain', 'charset':'utf-8',
    'model': "gpt-3.5-turbo",
    'temperature': str(temperature), ## change the temperature parameter to make it more variable
    'Connection': 'close'   
  }

  data_model= {'model': "gpt-3.5-turbo",
    'temperature': str(temperature)} ## change the temperature parameter to make it more variable

  ## process the previous questions for not repeated the same question
  for ccount in range(0,len(prev_questions)):
     body_question=prev_questions[ccount].split('\n')
     prev_question_string = prev_question_string+'\n -'+body_question[0]

  print(prev_question_string,'prev_question_string')  

  ## uncomment this if you want to make it a bit faster after you are accumulating questions
  ##if correctness == 0:
  ##   number_query=random.randint(0,20)
  ##   if (number_query % 2) == 0:
  ##       if number_query<=10:
  ##         data = f'Generate a (ONE) NEW question about general culture with {number_options} choices/answers specified with letters after the question, specify the correct answer at the end of the text \n'+'and please DO NOT repeat any of these following questions: '+ prev_question_string+ '\n'
  ##       else:
  ##         data = f'Generate a (ONE) NEW, easy, and random question with  {number_options} choices/answers, specify the choices with letters after the question, specify the correct answer at the end of the text \n'+' and please DO NOT repeat any of these following questions: '+ prev_question_string+ '\n'
  ##   else:
  ##         data = f'Generate a (ONE) NEW question about contemporary culture with {number_options} choices/answers specified with letters after the question, specify the correct answer at the end of the text \n'+'and please DO NOT repeat any of these following questions: '+ prev_question_string+ '\n'
  ##else:
  ##   number_query=random.randint(0,20)
  ##   if (number_query % 2) == 0:
  ##     if number_query<=10:
  ##       data =  f'Generate a (ONE) NEW hard/difficult question about any specific topic with {number_options} choices/answers specified with letters after the question, specify the correct answer at the end of the text \n'+'and please DO NOT repeat any of these following questions: '+ prev_question_string+ '\n'
  ##     else:
  ##       data = f'Generate a (ONE) NEW hard/difficult random question {number_options} choices/answers about any specific topic, specify the choices with letters after the question, specify the correct answer at the end of the text \n'+'and please DO NOT repeat any of these following questions: '+ prev_question_string+ '\n'
  ##   else:
  ##       data =  f'Generate a (ONE) VERY HARD! NEW question about any specific topic with {number_options} choices/answers specified with letters after the question, specify the correct answer at the end of the text \n'+'and please DO NOT repeat any of these following questions: '+ prev_question_string+ '\n'
  ## response = requests.post(url, headers=headers, data=data)  

  ## Adapts difficulty with two different types of queries grouping the previous question for no repeating a new question again for each session.
  ## if the previous question was answered correctly the difficult query is activated and more complicated topics are queried to SuperAPI
  number_options=random.randint(3,5)
  data1 = 'DO NOT repeat or generate again any of the following questions: '+ prev_question_string+ 'or any similar\n'
  if correctness == 0:
     number_query=random.randint(0,20)
     if (number_query % 2) == 0:
        if number_query<=10:
           data2 = f'Generate a NEW question about general culture with {number_options} choices/answers specified with letters after the question, specify the correct answer at the end of the text \n' 
        else:
           data2 = f'Generate a NEW, easy, and random question about any specific topic with {number_options} choices/answers, specify the choices with letters after the question, specify the correct answer at the end of the text \n'
     else:
           data2 = f'Generate a NEW question about contemporary culture with {number_options} choices/answers specified with letters after the question, specify the correct answer at the end of the text \n'
  else:
     number_query=random.randint(0,20)
     if (number_query % 2) == 0:
       if number_query<=10:
         data2 =  f'Generate a NEW hard/difficult question about any specific topic with {number_options} choices/answers specified with letters after the question, specify the correct answer at the end of the text \n'
       else:
         data2 = f'Generate a NEW hard/difficult random question {number_options} choices/answers about any specific topic, specify the choices with letters after the question, specify the correct answer at the end of the text \n'
     else:
         data2 =  f'Generate a NEW VERY HARD! question about any specific topic with {number_options} choices/answers specified with letters after the question, specify the correct answer at the end of the text \n'

  for attemp in range(10):
    try:
        response_ack = requests.post(url, headers=headers, json=data_model, data=data1)
        break
    except requests.exceptions.ChunkedEncodingError:
        time.sleep(1)

  print(response_ack,'response_ack')
  for attemp in range(10):
    try:
        response = requests.post(url, headers=headers, json=data_model, data=data2)
        break
    except requests.exceptions.ChunkedEncodingError:
        time.sleep(1)

  ## if the fecth is done correctly process the message from the chatbox
  if response.status_code == 200:
      result = response.content.decode('utf8')
      print(result,'result_request')
      ## check if the question has a number ahead
      if result[0]=='1' or result[0]=='2' or result[0]=='3' or result[0]=='4' or result[0]=='5' or result[0]=='6' or result[0]=='7' or result[0]=='8' or result[0]=='9':
         result=result[2:]
      result = result.replace('The correct answer is','Correct answer:')
      result = result.replace('Question:','')
      result = result.replace('Q:','')
      #result = result.replace('(','')
      if 'Correct' in result:
        if 'answer' in result:
          result_separated=result.split('Correct answer')
        if 'Answer' in result:
          result_separated=result.split('Correct Answer')   
      else:
        if 'Answer' in result:
          result_separated=result.split('Answer')
        elif 'answer' in result:
          result_separated=result.split('answer')
        #elif 'is' in result:
        #  result_separated=result.split('is')
        else:
          result_separated=result
      ## look for indeces in the list that start with answer and divided in get_response
      #result=' '.join(result)
      #print(result_separated,'result')
      if len(result_separated)==2:
          #result_separated[0]=result_separated[0].replace('(','')
          if result_separated[1][2]=='(' or result_separated[1][1]=='(' or result_separated[1][0]=='(':
              result_separated[1]=result_separated[1].replace('(','')
      #print(result_separated,'result_separated')
      #R=json.loads(result)
      #print(R)
      resp = "The question is loaded!\n"
      print(resp)
      return result_separated
  else:
     print("Error:", response.status_code)
     return "Error"

def get_response(answer,string_quiz,ccount,correct_count,len_quiz,string_prev):
  
   if answer.lower()=='yes' or answer.lower()=='y' or answer.lower()=='ok':
      return(str(ccount+1)+'.'+string_quiz[0],correct_count)
   elif answer.lower()=='no' or answer.lower()=='n':
      return('If you want to do another quiz please close and open the chatbox, or reply yes! If not \n End of the Quiz! closing the chatbox.\n',correct_count)
   else:
      ## look for the positions that start with answer with the ccount
      print(string_quiz,'string_quiz')
      len_quiz=len_quiz
      answer_def=string_prev
      answers=string_quiz[0]
      print(answer,string_prev,'values')
      if answer[0].lower() == string_prev[2].lower() or (answer.lower() in string_prev.lower() and answer.lower() == string_prev.lower()): ## evaluate correctness of the question 
         correct_answer='Correct! \n\n'
         correct_count=correct_count+1
      else:
         correct_answer='Incorrect, the correct answer is '+answer_def+'\n\n'

      ## validate the end of the Quiz here
      if ccount >= len_quiz:
           rate_correctness=(correct_count/len_quiz)*100
           d_answers=f'End of the Quiz! Your score was: {rate_correctness}% '+'\n reply yes and your information will be saved in the database..\n'
           def_answer=correct_answer+d_answers
      else:
           d_answers=answers
           def_answer=correct_answer+str(ccount+1)+'.'+d_answers ## join the options for printing again in the chat widget

      return def_answer, correct_count

if __name__ == "__main__":
    print("Let's solve the quiz! (type 'quit' to exit)")
    while True:
        #Start chosing to take the quiz or not"

        sentence = input("You: ")
        if sentence == "quit":
            break
        
        resp = get_response(sentence,string_quiz)
        print(resp)

