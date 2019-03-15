from flask import Flask, request, jsonify
#from flask_sslify import SSLify

app = Flask(__name__)
#sslify = SSLify(app)

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

        if data['object'] == "page":
            #print(data['entry'][0]['messaging'][0]['message'])
            print(data['entry'])

        return 'EVENT_RECEIVED' , 200

        if hubverify == "VERIFY_TOKEN" and hubmode == "subscribe": # Check data verify and mode
            return hubchallenge , 200 # Return 'CHALLENGE_ACCEPTED'

    elif request.method == 'GET':
        return 'GET' , 200

    else:
        return 'Forbidden' , 403

@app.route('/', methods=['GET','POST','PUT','DELETE'])
def index():
    if request.method == 'GET' or request.method == 'POST' or request.method == 'PUT' or request.method == 'DELETE':
        return 'Service Not Found', 404

if __name__ == '__main__':
    app.run()