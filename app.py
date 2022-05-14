from tkinter.tix import Tree
from flask import Flask,render_template,request
import random
from dataset import *
msgId=0

def chatbot_response(msg):
    res=''
    if int(msg)==1 and msgId==0:
        msgId=1
        res+='Here are some Top Rate places to visit: <br/>'
        for i in random.sample(Lakes,2):
            res+=i+'<br/>'
        res+='<br/><br/>'
        for i in random.sample(Sites,1):
            res+=i+'<br/>'
        res+='<br/><br/>'
        for i in random.sample(Historical,3):
            res+=i+'<br/>'
        res+='<br/><br/>'
        res+=Seasonal[1]    
        res+='<br/><br/>'
        res+='If you are looking for something specific, Please select: <br/> 1. Lakes <br/>2. Site Seeing <br/>3. Historical Places<br/>4. Seasonal Spots<br/>5. Main menu<br/>6. Say Goodbye <br/>'
    return res

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get')
def get_bot_response():
    userText=request.args.get('msg')
    return chatbot_response(userText)

if __name__=='__main__':
    app.run(debug=True)