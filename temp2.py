import os
import smtplib 
from flask import Flask,request,jsonify

email = os.environ.get("GMAIL_EMAIL")
password = os.environ.get("GMAIL_PASSWORD")

s = smtplib.SMTP('smtp.gmail.com', 587) 
  
s.starttls() 
  
# Authentication 
s.login(email,password) 
  
def sendmail(reciever,message):
    s.sendmail(email, reciever,  message) 

app = Flask(__name__)
@app.route("/",methods=['POST'])
def index():
    data = request.json;

    sendmail(data['email'],data['message'])
    return jsonify("Hi")

app.run(debug=True)
# creates SMTP session 

# message to be sent 

  
# terminating the session 
s.quit() 


# print(email,password)