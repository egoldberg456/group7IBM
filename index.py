from group7IBM import *

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/query/', methods=['POST', 'GET'])
def hit_it():
    