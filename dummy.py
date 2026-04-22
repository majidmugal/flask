from flask import Flask

api = Flask(__name__)

@api.route("/")
def home():
    return "home page"

@api.route("/facebook.com")
def about():
    return "about page"

@api.route("/772736726")
def contact():
    return "contact"




