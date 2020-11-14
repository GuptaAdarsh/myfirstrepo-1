js

import os
import smtplib 
from flask import Flask,request,jsonify


app = Flask(__name__)
@app.route("/",methods=['GET','POST'])
def index():
    print("Hi I'm called")
    return jsonify("Hi")

app.run(host='0.0.0.0',port=8080)
# creates SMTP session 

# message to be sent 

  
# terminating the session 
# s.quit() 


# print(email,password)
