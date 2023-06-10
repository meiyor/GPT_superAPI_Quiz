# GPT_superAPI_Quiz

This repository contents Python, JS, CSS, and html files necessary to run a SuperAPI/ChatGPT powered Quiz application with adaptable level of difficulty. The process of preparation, launching, and evaluation will be explained in this README file. Hope you enjoy the experience to evaluate this quiz application powered with one of the more novel APIs such as [SuperAPI](https://superapi.ai/). 

The queries to adapt difficulty and to bring questions to the chatbox in this appication are powered by this SuperAPI. In the following  steps we will explain how to execute this app. This app works better in Linux environments such as Ubuntu 20.04 or similar distributions and Mac OS X -> after installing any version of **Python>=3.8** and the requirements including in this repository. For deploying this in Windows it will be necessary to install [Cygwin](https://www.cygwin.com/) and [PuTTY](https://www.putty.org/) to manage the files and the connections.

# Preparation

First download all the files of this repository from the green button to download the code as zip file or using git clone, you need to have **git** installed in your system.

```git
git clone https://github.com/meiyor/GPT_superAPI_Quiz.git
```
Now install **pip** and **python-dev** in your system already having **Python>=3.8** already installed in your system

```bash
apt update
apt install python3-pip, python-dev
```
Having **pip** installed you must install the requirements included as the file **requirements.txt**. Then, go to the root folder and run this command to install the requirements that are necessary for running the app. Some of the requirements for this app are **Flask**, **Flask-cors**, **requests**, **Flask-SQLAlchemy**, and **subprocess**.

```bash
pip3 install -r requirements.txt
```
The next step is setting a **ngrok** account in [ngrok.com](https://ngrok.com/). Having an account you can download the latest version for linux and add it in the folder **/snap/bin/** if you want to do it more automatically you can use the **ngrok** file added in this repository and added in the folder **/snap/bin/** or installinng it using **snap** following this command.

```bash
snap install ngrok
```
Now, you need to authenticate your **ngrok** account running the command for authorization located in the **ngrok** dashboard, as it is shown in the following image and command.

<img src="https://github.com/meiyor/GPT_superAPI_Quiz/blob/main/images/image_ngrok.png" width="1000" height="150">

```bash
ngrok config add-authtoken 2QwQndCshan5Blls6oewbCPRUbe_2HG1EGCAE59mpJnEZhmZs
```
I added here my configuration key code but you must have one in your account dashboard when you activate yours. This process will let you activate a VPS in your local machine and will give you a public address where you can access your application. Now you need to allow permissions to port 5000 and 4040. You can do it with the **ufw** command.

```bash
ufw allow 5000
ufw allow 4040
```
These are the ports where your application will run the communication between **Flask** and **javascript**. More specifically the ngrok server and your application. The next step is loading/uploading the **ngrok** server following this command.

```bash
ngrok http 5000
```
After running this command you will obtain the following screen in your terminal giving the real-time status of the **ngrok** server and the public address where your application **app.py** will be located. I have marked in a red square (1) the address of the server and (2) the route of the public address that the application will have. Take these addresses into account for next steps.

<img src="https://github.com/meiyor/GPT_superAPI_Quiz/blob/main/images/ngrok_server_running.jpg" width="900" height="500">

Now we are are ready to deploy/launch the application on the **ngrok** server. 

# Launching/Deploying

The first step for deploying is setting app the SQL database as local file with **Flask-SQLAlchemy** and **SQLAlchemy**, to set the database tables you need to execute the following python command located in the root directory.

```python
python3 db_create.py
```
The next step integrates the **Flask** web app contained in the file **app.py** with the **javascript** engine included in the **static** folder as **app.js**. The user interface is constructed in the **templates** folder as the html file **base.html**. This will be loaded in the **ngrok** server from the port 5000. Therefore, in order to deploy the app you must open a new terminal (additional to the **ngrok** server one) and execute the following python command located in the root directory.

```python
python3 app.py
```

While both terminals are running you can open the browser of your preference. I suggest **firefox** or **Google Chrome** and copy and paste the address you obtained from the **ngrok** server as forwarding address. The one marked in the red squared. This address can be accessed from anywhere in the world while the **app.py** and the **ngrok** server are active/running. Having the server running we will obtain the following screen after accessing the **ngrok** forwarding address.

<img src="https://github.com/meiyor/GPT_superAPI_Quiz/blob/main/images/ngrok_first_page.jpg" width="900" height="500">

In this page you need to click the button **Visit site** and accept the regulations of the **ngrok** server. After you click it you will see the presentation of the  **Flask** and **SuperAPI** based web app running. It is presented as follows.

<img src="https://github.com/meiyor/GPT_superAPI_Quiz/blob/main/images/app_presentation.jpg" width="900" height="500">

In this web presentation we have the login section marked in the red square and the chat deploy button marked with a green squared. Now, we will continue with the testing and evaluation of this web app.

# Testing/Evaluation

The first you must do is to enter the user name and password in the login section and click on the **login** button. This will set your username and password information for the database and the chatbox. The chatbox will refer to you as your username all the time you are testing different questions/quizzes. After you set your login process a text will appear in the login status field as **new user 'username'**. Note that the database is not checking for repeated usernames or passwords yet. It generates a new field in the database each time a quiz is finalized. We can call it a quiz trial.

  <img src="https://github.com/meiyor/GPT_superAPI_Quiz/blob/main/images/newuser.jpg" width="900" height="500">
  
 **If and only after** you login you can click the chatbox button marked with the green squared. This embedded chatbox can offer you an infinite different amount of quizzes only if you want to continue to do more. When you click on it the chatbox it will ask if you want to solve a quiz with a random number of questions **between 3 and 15**. The chatbox will ask you first if you want to proceed with the quiz and you must answer **yes**, **y**, **Yes** or any equivalence in uppercase can be processed. After you answer **yes** you can start selecting the letters the chatbox will give you as options/answers. The following screen will appear after you answer/reply **yes** and start the quiz.
 
 <img src="https://github.com/meiyor/GPT_superAPI_Quiz/blob/main/images/first_question.jpg" width="900" height="500">
 
 Now, you must continue answering with the letters the chatbox is given to you. You can answer/reply **A** or **A.** or **A)** and whatever of these options can be processed with lower cases too. You have indefinitive time to answer each question, maybe some time contraints can be set in the future. While you are advancing in the quiz the chatbox will tell you how many questions you have answered correctly and when you finished the quiz they will tell you your percentage of **correctness**. If you reply **yes** when you finish your quiz the app will save your responses, correctness and the questions that have been asked to you in the database. 
 
 The following screen is obtained during the quiz evaluation, and there the chatbox will inform the user/you how many correct questions has been achieved.
 
 <img src="https://github.com/meiyor/GPT_superAPI_Quiz/blob/main/images/during_quiz.jpg" width="900" height="500">
 
 Subsequently, when the quiz ends the following screen appears showing the user/you (1) what was your level of correctness in the quiz and (2) if you want to save your information in the database.
 
 <img src="https://github.com/meiyor/GPT_superAPI_Quiz/blob/main/images/end_quiz.jpg" width="900" height="500">
 
 You can do the amount of quizzes you want replying **yes** to the quizzes continuation. Each quiz trial will be saved in the database. To stop the process you must reply **n**, **N**, **No** or similars in upper cases or clicking again in the chatbox deploy button. This will erase all the messages in the chatbox and you will start the quizzes from scratch, zero quizzes, and zero questions added in the **SuperAPI** query for adapting the difficulty. If you start from zero it is possible that some questions will be repeated. Therefore I suggest to do as many quizzes as possible to fill more the query and get more developed questions.
 
Finally, here we show a screenshot of the database showing the quiz trials I have until now, the number of correct answers, and the level of correctness. We can see the database file (called **database.db**) in any online SQL viewer. The id is generated randomly and it is the primary-key per quiz trial. The questions are saved in a Pickle format. Using **SQLAlchemy** it is easy convert all this question data to a list or json format.
 
 <img src="https://github.com/meiyor/GPT_superAPI_Quiz/blob/main/images/database.jpg" width="900" height="500">
 
  It tooks me a lot of work and time to put this **Flask** based web app in a public address. Most of the free and pay-as-go Linux servers that are available in the web, and support **Flask**, use **gunicorn** or **WSIG** and this represent a high web concurrency in the deploying process. These dedicated servers launch multiple threads and we need to contact the people who manages these servers to let them fire only one fork and one worker per session to avoid the usage of an extra database for the global variables in **app.py**. For the future we can make the **SuperAPI** query a bit more complex adding more data and more questions, and specifying more topics, but this is out of the scope of this web app. Hope you enjoy testing it and this work can be a starting point for more complete and ambicious projects.
 
 
 

