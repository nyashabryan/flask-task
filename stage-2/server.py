from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)


class MyPage:
    
    def __init__(self):
        self.css = url_for("static", filename = "main.css")
        self.profilepic =  url_for("static", filename = "images/profile.png")
        self.bankbrand = url_for("static", filename = "images/nblogo.png")
        self.profilename = "Nyasha Bryan"
        self.title = "Nyasha Bryan" + "'s Bank Portal"

@app.route("/")
def main_page():

    page = MyPage()
    
    return render_template("base.html", page = page)
