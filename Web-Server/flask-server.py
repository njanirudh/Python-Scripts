from flask import Flask , request
import json
import speech_recognition


app = Flask(__name__)

@app.route('/')
def index():
    return 'There is a server running here!'

@app.route('/speechRecog/', methods=["GET","POST"])
def speechRecognition():

    try:
        if request.method == "POST":
            print "POST request accepted !"
            print type(request.data)

            try:
                dict = json.loads(request.data)
            #dict = json.loads(request.data)
                print type(dict)
                print dict['key1']

                return 'POST Successful!!'

            except Exception as e:
                print e.__str__() + " Not a valid JSON"
                return 'Not a valid JSON'

        if request.method == "GET":
            print "GET request accepted !"
            return "GET??!"


    except Exception as e:
        print e

if __name__ == '__main__':
    app.run(debug=True, host='192.168.0.17')