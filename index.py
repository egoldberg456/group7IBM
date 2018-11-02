from group7IBM import *
from flask import request
import json

def parse_json():
    with open('questionnaire.json', 'r') as f:
        dict = json.load(f)

    print(dict)
    return dict

def give_answer(query):
    dict = parse_json()
    for word in query.split(' '):

        if word in dict['contextWords']:
            question = dict['contextWords'][word]
            answer = dict['questionnaire'][question]['answer']
            return answer

    return "Sorry, we do not have an answer to this question"

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/query/', methods=['POST', 'GET'])
def hit_it():
    query = request.form['query']
    return give_answer(query)