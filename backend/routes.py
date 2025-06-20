from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return 'Hello, hiiiii!'


@app.route('/reporter')
def reporter():
    return 'Reporter Bio'