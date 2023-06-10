var server = []
var user_global=[]

Promise.all([
  fetch("static/endpoint.txt").then(x => x.text())
]).then(([server]) => {
  console.log(server);
});

let btnLogin = document.querySelector('.btn_login')
let passwords = [];
let usernames = [];

class Chatbox {
    constructor() {
        this.args = {
            openButton: document.querySelector('.chatbox__button'),
            chatBox: document.querySelector('.chatbox__support'),
            sendButton: document.querySelector('.send__button')
        }

        this.state = false;
        this.messages = [];
    }

    display() {
        const {openButton, chatBox, sendButton} = this.args;

        openButton.addEventListener('click', () => this.toggleState(chatBox))

        sendButton.addEventListener('click', () => this.onSendButton(chatBox))

        btnLogin.addEventListener('click', () => this.addUser());

        const node = chatBox.querySelector('input');
        node.addEventListener("keyup", ({key}) => {
            if (key === "Enter") {
                this.onSendButton(chatBox)
            }
        })
    }

    addUser(){

    var newUser = document.querySelector('.input_username').value;
    var newPass = document.querySelector('.input_password').value;
    var status = document.querySelector('.span_result');

    usernames = usernames.concat(newUser);
    passwords = passwords.concat(newPass);
    console.log(usernames);
    console.log(passwords);

    status.innerHTML = "";
    status.appendChild(document.createTextNode("New User " + newUser + "!"))
    
    fetch(server+'/adduser', {
            method: 'POST',
            body: JSON.stringify({ user: newUser, pass: newPass }),
            mode: 'cors',
            headers: {
              'Content-Type': 'application/json'
            },
          })
           .then(ack => ack.json())
           .then(ack => {
            console.log(ack)
            textField.value = ''
        }).catch((error) => {
            console.error('Error:', error);
            this.updateChatText(chatbox)
            textField.value = ''
          });

     user_global=newUser

    }

    toggleState(chatbox) {
        this.state = !this.state;

        // show or hides the box
        if(this.state) {
            chatbox.classList.add('chatbox--active')
            fetch(server+'/ini', {
            method: 'POST',
            mode: 'cors',
            headers: {
              'Content-Type': 'application/json'
            },
          })
          .then(r => r.json())
          .then(r => {
          let msg_ini = { name: "User", message: user_global+'=>'+r.answer };
          this.messages.push(msg_ini);
          this.updateChatText(chatbox);
          textField.value = ''
          }).catch((error) => {
            console.error('Error:', error);
            this.updateChatText(chatbox)
            textField.value = ''
          });

        } else {
            chatbox.classList.remove('chatbox--active');
            /*for (let i = 0; i <= this.messages.length+100; i++) {
               this.messages.pop();
            }*/
            /*this.messages.pop();*/
            this.messages=[]; /* empty the array in an easier way */
            this.updateChatText(chatbox);
            textField.value = ''
        }
    }

    async onSendButton(chatbox) {
        var textField = chatbox.querySelector('input');
        let text1 = textField.value
        if (text1 === "") {
            return;
        }

        let msg1 = { name: "User", message: user_global+': '+text1 }
        
        this.messages.push(msg1);

        await fetch(server+'/predict', {
            method: 'POST',
            body: JSON.stringify({ message: text1 }),
            mode: 'cors',
            headers: {
              'Content-Type': 'application/json'
            },
          })
           .then(r => r.json())
           .then(r => {
            let msg2 = { name: "User", message: r.answer };
            this.messages.push(msg2);
            this.updateChatText(chatbox)
            textField.value = ''

        }).catch((error) => {
            console.error('Error:', error);
            this.updateChatText(chatbox)
            textField.value = ''
          });
    }

    updateChatText(chatbox) {
        var html = '';
        this.messages.slice().reverse().forEach(function(item, index) {
            if (item.name === "User")
            {
                html += '<div class="messages__item messages__item--visitor">' + item.message + '</div>'
            }
            else
            {
                html += '<div class="messages__item messages__item--operator">' + item.message + '</div>'
            }
          });

        const chatmessage = chatbox.querySelector('.chatbox__messages');
        chatmessage.innerHTML = html;
    }
}


const chatbox = new Chatbox();
chatbox.display();
