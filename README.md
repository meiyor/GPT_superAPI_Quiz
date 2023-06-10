# GPT_superAPI_Quiz

This repository contents Python, JS, CSS, and html files necessary to run a SuperAPI/ChatGPT powered Quiz application with adaptable level of difficulty. The process of preparation, launching, and evaluation will be explained in this README file. Hope you enjoy the experience to evaluate this quiz application powered with one of the more novel APIs such as [SuperAPI](https://superapi.ai/). 

The queries to adapt difficulty and to bring questions to the chatbox in this appication are powered by this API. In the following  steps we will explain how to execute this app. This app works better in Linux environments such as Ubuntu 20.04 or similar distributions and Mac OS X after installing any version **Python>=3.8** and the requirements including here. For deploying in Windows it will be necessary [Cygwin](https://www.cygwin.com/) and [PuTTY](https://www.putty.org/) to manage the files and the connections.

# Preparation

First download all the files of this repository from the green button to download the code as zip file or using git clone, you need to have **git** installed in your system.

```git
git clone https://github.com/meiyor/GPT_superAPI_Quiz.git
```
Now install **pip** and **python-dev** in your system already having **Python>=3.8** installed in your system

```bash
apt update
apt install python3-pip, python-dev
```
Having **pip** installed you must install the requirements included as the file **requirements.txt**. Then, go to the root folder and run this command to install the requirements necessary for running the app. Some of the requirements for this app are **Flask**, **Flask-cors**, **requests**, **Flask-SQLAlchemy**, **subprocess**, and  **SQLAlchemy**.

```bash
pip3 install -r requirements.txt
```
The next step is setting a **ngrok** account in [ngrok.com](https://ngrok.com/). Having an account you can download the latest version for linux and added in the folder **/snap/bin/** if you want to do it more automatically you can use the **ngrok** file added in this repository and added in the folder **/snap/bin/** or installinng it using **snap**.

```bash
snap install ngrok
```
Now, you need to authenticate your **ngrok** account running the command set for authorization in the **ngrok** dashboard as it shown in the following image and command.

<img src="https://github.com/meiyor/GPT_superAPI_Quiz/blob/main/images/image_ngrok.png" width="900" height="250">

```bash
ngrok config add-authtoken 2QwQndCshan5Blls6oewbCPRUbe_2HG1EGCAE59mpJnEZhmZs
```
I added there my configuration key but you must have one in your account when you activate yours. This process will let you activate a VPS in your local machine and will give you a public address where you can access your application. Now you need to allow permissions to port 5000 and 4040 and you can do it with the **ufw** command.

```bash
ufw allow 5000
ufw allow 4040
```
These are the ports where your application will run more specifically the ngrok server and your application. The next step is loading the **ngrok** server following the this command.

```bash
ngrok http 5000
```
After running this command you will  obtain the following screen in your terminal giving the real-time status of the **ngrok** server and the public address where your application will be ending in .app. I have marked in a red square (1) the address of the server and (2) the route of the public address that the application will have. Take this address into account for next steps.

<img src="https://github.com/meiyor/GPT_superAPI_Quiz/blob/main/images/ngrok_server_running.jpg" width="900" height="500">

Now we are are ready to deploy/launch the application on the **ngrok** server. 

# Launching/Deploying

The first step for deploying is setting app the SQL database as local file with **Flask-SQLAlchemy** and **SQLAlchemy**, to set the database tables you need to execute the following python command in the root directory.

```python
python3 db_create.py
```
The next step integrates the **Flask** web app contained in the file **app.py** with the **javascript** engine included in the **static** folder as **app.js**. The user interface is constructed in the **templates** folder as the html file **base.html**. This will be loaded in ngrok from the port 5000. Therefore, in order to deploy the app you must open a new terminal (additional to the **ngrok** server one) and execute the following python command in the root directory.

```python
python3 app.py
```

While both terminals are running you can open the browser of your preference, I suggest **firefox** or **Google Chrome** and copy and paste the address you obtained from the **ngrok** server as forwarding address. The one marked in the red squared. This address can be accessed from anywhere in the world while the **app.py** and the **ngrok** server are active/running. Next we will obtained the following screen after accessing the **ngrok** forwarding address.

<img src="https://github.com/meiyor/GPT_superAPI_Quiz/blob/main/images/ngrok_first_page.jpg" width="900" height="500">

In this page you need to click the button **Visit site** and accept the regulations of the **ngrok** server, after you click it you will see the presentation **Flask** and **SuperAPI** based web app running.

<img src="https://github.com/meiyor/GPT_superAPI_Quiz/blob/main/images/app_presentation.jpg" width="900" height="500">
