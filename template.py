from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home(): 
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/services")
def services():
    return render_template("services.html")  

@app.route("/profile")
def profile():
    return render_template("profile.html")  

@app.route("/login")
def login():
    return render_template("login.html")