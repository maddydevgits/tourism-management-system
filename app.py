from tkinter.tix import Tree
from flask import Flask,render_template,request
import random
from dataset import *
msgId=0

def hotelDetails(z):
    k=''
    k+='Hotel: '+str(z[0])+'<br/>'
    k+='Cost: '+str(z[1])+'<br/>'
    k+='Amenities: <br/>'
    for i in range(len(z[3])):
        k+=z[3][i]+'<br/>'
    k+='<br/>'
    return(k)

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
    elif(int(msg)==2 and msgId==0):
        res+='<b>Here are some Top Recommended Restaurants</b><br/>'
        z=random.sample(Rest[0],2)
        res+=z[0]+'<br/>'
        res+=z[1]+'<br/>'
        z=random.sample(Rest[1],1)
        res+=z[0]+'<br/>'
        z=random.sample(Rest[2],1)
        res+=z[0]+'<br/>'
        res+='<br/><br/>'
        res+='Please select your price range for better recommendation: <br/>1. Royal (Cost for two: Rs. 3500) <br/>2. Premium(Cost for two: Rs. 1500) <br/>3. Classic(Cost for two: Rs. 700) <br/>4. Return to Main Menu <br/>5. Exit'
        msgId=2
    elif((msgId==2) and int(msg)==1):
        res+='<b>Here is a list of Royal Restaurants of the City</b><br/>'
        for i in range(len(Rest[0])):
            res+=Rest[0][i]+'<br/>'
        res+='<br/><br/>'
        res+='Please select your price range for better recommendation: <br/>1. Royal (Cost for two: Rs. 3500) <br/>2. Premium(Cost for two: Rs. 1500) <br/>3. Classic(Cost for two: Rs. 700) <br/>4. Return to Main Menu <br/>5. Exit'
    elif((msgId==2) and int(msg)==2):
        res+='<b>Here is a list of Best Premium Restaurants of the City</b><br/>'
        for i in range(len(Rest[1])):
            res+=Rest[1][i]+'<br/>'
        res+='<br/><br/>'
        res+='Please select your price range for better recommendation: <br/>1. Royal (Cost for two: Rs. 3500) <br/>2. Premium(Cost for two: Rs. 1500) <br/>3. Classic(Cost for two: Rs. 700) <br/>4. Return to Main Menu <br/>5. Exit'
    elif((msgId==2) and int(msg)==3):
        res+='<b>Here is a list of Top Classic Restaurants of the City</b><br/>'
        for i in range(len(Rest[2])):
            res+=Rest[2][i]+'<br/>'
        res+='<br/><br/>'
        res+='Please select your price range for better recommendation: <br/>1. Royal (Cost for two: Rs. 3500) <br/>2. Premium(Cost for two: Rs. 1500) <br/>3. Classic(Cost for two: Rs. 700) <br/>4. Return to Main Menu <br/>5. Exit'
    elif((msgId==2) and int(msg)==4):
        res+='Tell me What Can I do for you? <br/>1. Recommend a Tourist Spot <br/>2. Recommend some good Restaurants <br/>3. Tell some Good Hotels <br/>4. Checkout our Exclusive Packages <br/>5. Exit'
        msgId=0
    elif((msgId==2) and int(msg)==5):
        res+='Time to say Goodbye, Hope to see you soon <br/>Happy Travelling'
        msgId=0
    elif(int(msg)==3 and msgId==0):
        res+'Here are some Handpicked Hotels you may like:'
        z=random.sample(Hotel[0],1)
        res+=hotelDetails(z[0])
        z=random.sample(Hotel[1],1)
        res+=hotelDetails(z[0])
        z=random.sample(Hotel[2],1)
        res+=hotelDetails(z[0])
        res+='<br/><br/>'
        res+='Please Select your Hotel Price Range for better recommendation: <br/>1. Royal (Cost per Night: Rs.45,500) <br/>2. Premium(Cost per Night: Rs. 15,500) <br/>3. Classic (Cost Per Night: Rs. 5000) <br/>4. Return to Main Menu <br/>5. Say Goodbye <br/>'
        msgId=3
    elif((msgId==3) and int(msg)==1):
        res+='<b>Here is a list of Royal Hotels for you:</b><br/>'
        for i in range(len(Hotel[0])):
            res+=hotelDetails(Hotel[0][i])+'<br/>'
        res+='<br/><br/>'
        res+='Please Select your Hotel Price Range for better recommendation: <br/>1. Royal (Cost per Night: Rs.45,500) <br/>2. Premium(Cost per Night: Rs. 15,500) <br/>3. Classic (Cost Per Night: Rs. 5000) <br/>4. Return to Main Menu <br/>5. Say Goodbye <br/>'
    elif((msgId==3) and int(msg)==2):
        res+='<b>Here is a list of Best Premium Hotels for you: </b><br/>'
        for i in range(len(Hotel[1])):
            res+=hotelDetails(Hotel[1][i])+'<br/>'
        res+='<br/><br/>'
        res+='Please Select your Hotel Price Range for better recommendation: <br/>1. Royal (Cost per Night: Rs.45,500) <br/>2. Premium(Cost per Night: Rs. 15,500) <br/>3. Classic (Cost Per Night: Rs. 5000) <br/>4. Return to Main Menu <br/>5. Say Goodbye <br/>'
    elif((msgId==3) and int(msg)==3):
        res+='<b>Here is a list of Top Classic Hotels for you: </b><br/>'
        for i in range(len(Hotel[2])):
            res+=hotelDetails(Hotel[2][i])+'<br/>'
        res+='<br/><br/>'
        res+='Please Select your Hotel Price Range for better recommendation: <br/>1. Royal (Cost per Night: Rs.45,500) <br/>2. Premium(Cost per Night: Rs. 15,500) <br/>3. Classic (Cost Per Night: Rs. 5000) <br/>4. Return to Main Menu <br/>5. Say Goodbye <br/>'
    elif((msgId==3) and int(msg)==4):
        res+='Tell me What Can I do for you? <br/>1. Recommend a Tourist Spot <br/>2. Recommend some good Restaurants <br/>3. Tell some Good Hotels <br/>4. Checkout our Exclusive Packages <br/>5. Exit'
        msgId=0
    elif((msgId==3) and int(msg)==5):
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