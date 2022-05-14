from tkinter.tix import Tree
from flask import Flask,render_template,request
import random
from dataset import *
msgId=0

def chatbot_response(msg):
    global msgId
    res=''
    if int(msg)==1 and msgId==0:
        msgId=1
        res+='<b>Here are some Top Rate places to visit:</b> <br/>'
        for i in random.sample(Lakes,2):
            res+=i+'<br/>'
        res+='<br/>'
        for i in random.sample(Sites,1):
            res+=i+'<br/>'
        res+='<br/>'
        for i in random.sample(Historical,3):
            res+=i+'<br/>'
        res+='<br/>'
        res+=Seasonal[1]+'<br/>'    
        res+='<br/><br/>'
        res+='If you are looking for something specific, Please select: <br/> 1. Lakes <br/>2. Site Seeing <br/>3. Historical Places<br/>4. Seasonal Spots<br/>5. Main menu<br/>6. Say Goodbye <br/>'
    elif((msgId==1) and int(msg)==1):
        res+='<b>Here is the list of Top 7 Lakes in the City</b> <br/>'
        for i in range(len(Lakes)):
            res+=Lakes[i]+'<br/>'
        res+='<br/><br/>'
        res+='If you are looking for something specific, Please select: <br/> 1. Lakes <br/>2. Site Seeing <br/>3. Historical Places<br/>4. Seasonal Spots<br/>5. Main menu<br/>6. Say Goodbye <br/>'
    elif((msgId==1) and (int(msg)==2)):
        res+='<b>Here is the list of Top 3 Site Seeing Places in the City</b> <br/>'
        for i in range(len(Sites)):
            res+=Sites[i]+'<br/>'
        res+='<br/><br/>'
        res+='If you are looking for something specific, Please select: <br/> 1. Lakes <br/>2. Site Seeing <br/>3. Historical Places<br/>4. Seasonal Spots<br/>5. Main menu<br/>6. Say Goodbye <br/>'
    elif((msgId==1) and int(msg)==3):
        res+='<b>Here is the lis of Top 14 Historical Places of the City</b> <br/>'
        for i in range(len(Historical)):
            res+=Historical[i]+'<br/>'
        res+='<br/><br/>'
        res+='If you are looking for something specific, Please select: <br/> 1. Lakes <br/>2. Site Seeing <br/>3. Historical Places<br/>4. Seasonal Spots<br/>5. Main menu<br/>6. Say Goodbye <br/>'
    elif((msgId==1) and int(msg)==4):
        res+='<b>Here is list of some Famous Seasonal Fests of the City</b> <br/>'
        for i in range(len(Seasonal)):
            res+=Seasonal[i]+'<br/>'
        res+='<br/><br/>'
        res+='If you are looking for something specific, Please select: <br/> 1. Lakes <br/>2. Site Seeing <br/>3. Historical Places<br/>4. Seasonal Spots<br/>5. Main menu<br/>6. Say Goodbye <br/>'
    elif((msgId==1) and int(msg)==5):
        res+='Tell me What Can I do for you? <br/>1. Recommend a Tourist Spot <br/>2. Recommend some good Restaurants <br/>3. Tell some Good Hotels <br/>4. Checkout our Exclusive Packages <br/>5. Exit'
        msgId=0
    elif((msgId==1) and int(msg)==6):
        res+='Time to say Goodbye, Hope to see you soon <br/>Happy Travelling'
        msgId=0

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