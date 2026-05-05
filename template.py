from flask import Flask
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] ="sqlite:///abc.db"

db = SQLAlchemy(app)


class user(db.Model):
        id = db.Column(db.Integer , primary_key = True)
        name = db.Column(db.String, nullable = False)
        email = db.Column(db.String, nullable = False, unique = True)
        password = db.Column(db.String, nullable = False )
        collage = db.Column(db.String)
        
with app.app_context():
    db.create_all()

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
    data = user.query.all()
    return render_template("profile.html", fe_data = data)  

@app.route("/login")
def login():
    return render_template("login.html")

# @app.route("/registration")
# def registration():
#     return render_template("registerform.html")


@app.route("/form_args")
def form_args():
    return request.args


@app.route("/log_in" ,methods = ["post"])
def form_form():
    return request.form
    # return "login successfull"


@app.route("/register" ,methods = ["GET", 'POST'])
def register():
    if request.method == "POST":

        a= user(
            name = request.form.get("name"),
            email = request.form.get("email"),
            password = request.form.get("password"),
            collage = request.form.get("collage")

        )

        db.session.add(a)
        db.session.commit()

        return "user created successfully"
    
    return render_template("register.html")


@app.route("/Search")
def search():
    if request.args:
        collage = request.args["collage_name"]
        data = user.query.filter(user.collage == collage).all()

        return render_template("Search.html", fe_data = data)
    
    return render_template("Search.html")


   
    