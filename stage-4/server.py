from flask import Flask
from flask import render_template
from flask import url_for
from flask import session
from flask import redirect
from flask import request

import requests
import json

import time

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

class MyPage:
    
    def __init__(self, user):
        self.css = url_for("static", filename = "main.css")
        self.profilepic =  url_for("static", filename = "images/profile.png")
        self.bankbrand = url_for("static", filename = "images/nblogo.png")
        self.profilename = user.name
        self.title = user.name + "'s Bank Portal"
        self.user = user

class User:

    def __init__(self, name, balanceHistory = None):
        self.name = name
        if balanceHistory == None:
            self.balanceHistory = []

        else:
            self.balanceHistory = balanceHistory

# A predefined history which is loaded when the page originally starts up


predefHistory = [["01 May 2018", "55.36"], ["05 May 2018", "155.36"], ["10 May 2018", "689.36"], ["11 May 2018", "55.36"]]
user =  User("Nyasha Bryan", predefHistory)

#Method to get the BitCoin Exchange Rate

def getBitRate():

    data = {
        "pair": "XBTZAR"
    }

    r = requests.get("https://api.mybitx.com/api/1/ticker")
    try:
        return eval(json.loads(r.json())[0]['ask'])
    catch:
        return 0
    

@app.route("/")
def main_page():
    global user
    if 'balance' in session:
        try:
            user.balanceHistory.append([time.strftime("%d %b %Y"), session['balance']])
        except:
            pass
    
    page = MyPage(user)
    page.bitRate = getBitRate()
    return render_template("base.html", page = page)



@app.route("/enterBalance", methods = ["POST", "GET"])
def enterBalance():

    if request.method == "POST":
        try:
            session['balance'] = round(eval(request.form['balance']), 2)
        except:
            pass
            # Maybe implement some sort of form control here. 
    return redirect(url_for("main_page"))

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


"""
    The genius is in making the session have a variable balanceHistory which is actually a 
    list. Now when rendering the page again, everything in the list
    must be added one by one to the table.
"""

