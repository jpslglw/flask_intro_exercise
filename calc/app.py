# Put your app in here.

from flask import Flask, request 
from operations import add, sub, mult, div # importing support functions

app = Flask(__name__) # server creation

@app.route('/add') 
def add_num():
    """adding a+b with add(a,b) func"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    res = add(a,b)
    return str(res)

@app.route('/sub') 
def sub_num():
    """subtracting a-b with sub(a,b) func"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    res = sub(a,b)
    return str(res)

@app.route('/mult') 
def mult_num():
    """multiplying a*b with mult(a,b) func"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    res = mult(a,b)
    return str(res)

@app.route('/div') 
def div_num():
    """dividing a/b with div(a,b) func"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    res = div(a,b)
    return str(res)