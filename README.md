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
apt install python3-pip
```
Having **pip** installed you must install the requirements included as the file **requirements.txt**. Then, go to the root folder and run this command to install the requirements necessary for running the app.

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
I added there my configuration key but you must have one in your account when you activate yours. This process will let you activate a VPS in your local machine and will give you a public address where you can access your application.

