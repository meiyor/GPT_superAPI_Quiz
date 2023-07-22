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
  if temperature > 1.0:
     temperature=1.0
  ## request connection with SuperAPI interface 
  url = 'https://superapi.ai/v2/juan-manuelmayor-torres/chat-quiz'
  headers = {
    'accept': 'text/plain',
    'Authorization': 'Bearer r:34a30d828729d2b75db89a9ce164f1b7',
    'Content-Type': 'text/plain', 'charset':'utf-8',
    'model': "gpt-3.5-turbo",
    'temperature': str(temperature), ## change the temperature parameter to make it more variable
    'frequency_penalty': str(1.0),
    'presence_penalty': str(1.0),
    'Connection': 'close'
  }

  data_model= {'model': "gpt-3.5-turbo",
    'frequency_penalty': str(1.0),
    'presence_penalty': str(1.0),
    'temperature': str(temperature)} ## change the temperature parameter to make it more variable

  ## process the previous questions for not repeated the same question
  for ccount in range(0,len(prev_questions)):
     body_question=prev_questions[ccount].split('\n')
     if ccount == 0:
           prev_question_string = prev_question_string+' or -'+body_question[0]+'\n'
     else:
           prev_question_string = prev_question_string+' or -'+body_question[0]+'\n'
  #prev_question_string = prev_question_string+'\n'
  print(prev_question_string,'prev_question_string')
  
  if len(prev_questions)>0:
       last_question=prev_questions[len(prev_questions)-1].split('\n')
  else:
       last_question=''
  ## combine the queries depending on a random number
  number_selection = random.randint(0,1000)+500
  number_options=random.randint(3,5)
  data1 = 'DO NOT WRITE/REPEAT ANY of the following questions:'+ prev_question_string+'\n'
  if correctness == 0:
     number_query=random.randint(0,20)
     if (number_query % 2) == 0:
        if number_query<=10:
          if len(prev_questions)==0:
              data2 = f'Write a NEW easy question about general culture with {number_options} choices/answers specified with letters after the question, specify the correct answer at the end of the text in a new line, do not repeat this question'
          else:
              data2 = 'Write a NEW easy question, easier than this question: -' + last_question[0] + f', about general culture with {number_options} choices/answers specified with letters after the question, specify the correct answer at the end of the text  in a new line, do not repeat this question'
        else:
          if len(prev_questions)==0:
              data2 = f'Write a NEW, easy, and random question about any specific topic with {number_options} choices/answers, specify the choices with letters after the question, specify the correct answer at the end of the text in a new line, , do not repeat this question'
          else:
              data2 = 'Write a NEW, easy, and random question, easier than this question: -' + last_question[0] + f', about any specific topic with {number_options} choices/answers, specify the choices with letters after the question, specify the correct answer at the end of the text in a new line, do not repeat this question'
     else:
          if len(prev_questions)==0:
              data2 = f'Write a NEW easy question about contemporary culture with {number_options} choices/answers specified with letters after the question, specify the correct answer at the end of the text in a new line, do not repeat this question'
          else:
              data2 = 'Write a NEW easy question, easier than this question: -' + last_question[0] +  f', about contemporary culture with {number_options} choices/answers specified with letters after the question, specify the correct answer at the end of the text in a new line, do not repeate this question'
  else:
     number_query=random.randint(0,20)
     if (number_query % 2) == 0:
       if number_query<=10:
          if len(prev_questions)==0:
              data2 = f'Write a NEW hard/difficult question about any specific topic with {number_options} choices/answers specified with letters after the question, specify the correct answer at the end of the text in a new line, do not repeat this question'
          else:
              data2 = 'Write a NEW hard/difficult question, harder than this question: - ' + last_question[0] + f', about any specific topic with {number_options} choices/answers specified with letters after the question, specify the correct answer at the end of the text in a new line, do not repeat this question'
       else:
          if len(prev_questions)==0:
              data2 = f'Write a NEW hard/difficult random question with {number_options} choices/answers about any specific topic, specify the choices with letters after the question, specify the correct answer at the end of the text in a new line,  do not repeat this question'
          else:
              data2 = 'Write a NEW hard/difficult random question, harder than this question: - ' + last_question[0] + f', with {number_options} choices/answers about any specific topic, specify the choices with letters after the question, specify the correct answer at the end of the text in a new line, do not repeat this question'
     else:
          if len(prev_questions)==0:
              data2 = f'Write a NEW VERY HARD! question about any specific topic with {number_options} choices/answers specified with letters after the question, specify the correct answer at the end of the text in a new line, , do not repeat this question'
          else:
              data2 = 'Write a NEW VERY HARD! question, harder than this question: - ' + last_question[0] +  f', about any specific topic with {number_options} choices/answers specified with letters after the question, specify the correct answer at the end of the text in a new line, do not repeat this question'

  if number_selection < 550:
      ## requests variation depending on the random number
      for attemp in range(10):
        try:
            response_ack = requests.post(url, headers=headers, json=data_model, data=data1.encode('utf-8').decode('utf-8','ignore').encode('latin-1','ignore').decode('utf-8','ignore'))
            time.sleep(1)
            break
        except requests.exceptions.ChunkedEncodingError:
            time.sleep(1)

      for attemp in range(10):
        try:
            response = requests.post(url, headers=headers, json=data_model, data=data2.encode('utf-8').decode('utf-8','ignore').encode('latin-1','ignore').decode('utf-8','ignore'))
            time.sleep(1)
            break
        except requests.exceptions.ChunkedEncodingError:
            time.sleep(1)
      print(response_ack,'response_ack')
  else:
      ## requests variation depending on the random number
      for attemp in range(10):
        try:
            response = requests.post(url, headers=headers, json=data_model, data=data1.encode('utf-8').decode('utf-8','ignore').encode('latin-1','ignore').decode('utf-8','ignore')+data2.encode('utf-8').decode('utf-8','ignore').encode('latin-1','ignore').decode('utf-8','ignore'))
            time.sleep(1)
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
      result = result.replace('NEW QUESTION:','')
      result = result.replace('NEW difficult question:','')
      result = result.replace('NEW VERY HARD! question:','')
      result = result.replace('NEW VERY HARD! QUESTION:','')
      result = result.replace('NEW VERY HARD question:','')
      result = result.replace('NEW easy question:','')
      result = result.replace('NEW VERY HARD QUESTION:','')
      result = result.replace('NEW hard/difficult question:','')
      result = result.replace('NEW hard/difficult QUESTION:','')
      result = result.replace('NEW difficult random question:','')
      result = result.replace('NEW hard question:','')
      result = result.replace('NEW very hard question:','')
      result = result.replace('NEW HARD QUESTION:','')
      result = result.replace('NEW hard/difficult random question:','')
      result = result.replace('NEW hard/difficult random QUESTION:','')
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
          count_char=result_separated[1].count(':')
          if count_char>=2:
             #pos=result_separated[1].find(':')
             result_separated[1].replace(':','')
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

