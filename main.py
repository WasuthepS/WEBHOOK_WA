from flask import Flask, request, jsonify, render_template
import dbchat
import bot_sent_messages
import requests
import requset_post
import find_stage
import os
import dialogflow
import json
#import pusher

#from flask_sslify import SSLify

app = Flask(__name__)

# sslify = SSLify(app,subdomains=True)
# EAALNyShJXH8BAOo5o88mnzJu43t8TqeBl42qGNOna3Gx1RBhPUGvBcFB6tY6RXYNH7Df68Aj6IK3KMtRw9bBiHkeD5h6X7kAAlAxgFb5fiHbp3Udhx2sY7FET8xfIbz5tiLsFynlhDGz0W30Fz4FQFcuL1KZClwZAZA3U0l4gZDZD
@app.route('/webhook', methods=['GET','POST'])
def webhook():
    if request.method == 'GET':
        VERIFY_TOKEN = "ga75HpoblY9qBtOKo2m8QXauNvBoKQzt" # Key for Verify Token
        hubverify = request.args.get('hub.verify_token') # Get Verify Key tokem
        hubchallenge = request.args.get('hub.challenge') # For return to Facebook must to 'CHALLENGE_ACCEPTED'
        hubmode = request.args.get('hub.mode') # Mode must to 'subscribe'
        
        if hubverify == VERIFY_TOKEN and hubmode == "subscribe": # Check data verify and mode
            print('WEBHOOK_VERIFIED')
            return hubchallenge , 200 # Return 'CHALLENGE_ACCEPTED'
        
        else:
            return 'You Wrong Something' , 200

    elif request.method == 'POST':
        data = request.get_json()
        
        #data_user_stage=dbchat.db_select("user_stage","_all_docs")#chack data key access token
        #total_rows=(data_user_stage['total_rows'])#chack number of key access token
        key_1 = data['entry'][0]['messaging'][0]['sender']['id']#user_id_from_user
        r=requests.get('http://10.17.2.210:5984/user_stage/_design/find_user_stage/_view/find_user_stage_v1?key='+key_1)
        data_stage=r.text
        data_stage=r.json()
        stage_status_1=data_stage['rows']
        total_rows_user_stage=data_stage['total_rows']

        #print(data_id)/
        if data['object'] == "page" :#and stage_status_1 !=[] :
            if total_rows_user_stage  != 0:# and stage_status_1 != [] :
                #if stage_status_1 != [] : wati for edit
                user_id = data['entry'][0]['messaging'][0]['sender']['id']#user_id_from_user
                key = '"'+ user_id +'"'
                r=requests.get('http://10.17.2.210:5984/user_stage/_design/find_user_stage/_view/find_user_stage_v1?key='+key)
                data_stage=r.text
                data_stage=r.json()
                stage_status=data_stage['rows'][0]['value'][0]

                if stage_status == "1" :
                    requset_post.get_keytoken()

                ###################3if stage_status == "2" :
               
                else:
                    print(bot_sent_messages.post(data))
                    return "no stage_status"
            else:
                print(dbchat.db_insert("db-chat",data))
                print(bot_sent_messages.post(data))
        return 'EVENT_RECEIVED' , 200

        if hubverify == VERIFY_TOKEN and hubmode == "subscribe": # Check data verify and mode
            return hubchallenge , 200 # Return 'CHALLENGE_ACCEPTED'

    elif request.method == 'GET':
        return 'GET' , 200

    else:
        return 'Forbidden' , 403


#####@app.route('/dialogflow', methods=['GET','POST'])
#
#
#
#
#
#
@app.route('/dialogflow', methods=['POST'])
def get_movie_detail():
    data = request.get_json()
    print(data)
    reply = {
        "fulfillmentText": "response",
    }
    
    return jsonify(reply)

def detect_intent_texts(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    
    if text:
        text_input = dialogflow.types.TextInput(
            text=text, language_code=language_code)
        query_input = dialogflow.types.QueryInput(text=text_input)
        response = session_client.detect_intent(
            session=session, query_input=query_input)
        
        return response.query_result.fulfillment_text


@app.route('/send_message', methods=['POST'])
def send_message():
    socketId = request.form['socketId']
    message = request.form['message']
    project_id = os.getenv('DIALOGFLOW_PROJECT_ID')
    fulfillment_text = detect_intent_texts(project_id, "unique", message, 'en')
    response_text = { "message":  fulfillment_text }
    

    #pusher_client.trigger('movie_bot', 'new_message',
    #                    {'human_message': message, 'bot_message': fulfillment_text})
                        
    return jsonify(response_text)

#
#
#
#
#
#

@app.route('/', methods=['GET','POST','PUT','DELETE'])
def index():
    if request.method == 'GET' or request.method == 'POST' or request.method == 'PUT' or request.method == 'DELETE':
        return 'Service Not Found', 404

if __name__ == '__main__':
    app.run(debug=True)
