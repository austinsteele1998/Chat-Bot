from flask import Flask, jsonify, request
from flask_cors import CORS
import Predict_api
import json
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
from keras.models import load_model


model = load_model('chatbot_model.h5')
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))

# configuration

DEBUG = False

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

intents = json.loads(open('intents.json').read())

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

# dummy chat/ test 
@app.route('/dummy_chat', methods=['POST'])
def dumpy_answer():
    return jsonify({'message': request.json['message']})

# call ai_chat engine
@app.route('/ai_chat', methods=['POST'])
def ai_answer():
    # get the user input
    msg = request.json['message']
    ints = Predict_api.predict_class(msg)
    res = Predict_api.getResponse(ints, intents)
    return jsonify({'message': res})


if __name__ == '__main__':
    app.run(threaded=False)

