from flask import Flask # import flask
app = Flask(__name__) # server creation

@app.route('/welcome') # @ is decorator
def say_welcome():
    return 'welcome'

@app.route('/welcome/home') # @ is decorator
def say_home():
    return 'welcome home'

@app.route('/welcome/back') # @ is decorator
def say_back():
    return 'welcome back'