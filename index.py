from group7IBM import *
from flask import request

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/query/', methods=['POST'])
def hit_it():
    query = request.form['query']
    


