from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def home(): 
    return render_template("home.html"),503

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

@app.route("/registration")
def registration():
    return render_template("registerform.html")


@app.route("/form_args")
def form_args():
    return request.args


@app.route("/log_in" ,methods = ["post"])
def form_form():
    return request.form
    # return "login successfull"


@app.route("/registeration" ,methods = ["post"])
def registration_form():
   
    return request.form
    # return "registration succecfull"