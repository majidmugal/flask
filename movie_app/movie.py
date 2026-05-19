from flask import Flask
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie.db"
database = SQLAlchemy(app)

class Movie( database.Model ):
    id = database.Column(database.Integer , primary_key = True)
    name = database.Column(database.String)
    description = database.Column(database.String)
    rating = database.Column(database.String)
    duration = database.Column(database.String)


with app.app_context():
    database.create_all()

    
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/add")
def create():
    return render_template("add.html")


@app.route("/add_movie", methods=["POST"])
def add_movie():

    obj = Movie (
        name = request.form.get("name"),
        description = request.form.get("description"),
        rating = request.form.get("rating"),
        duration = request.form.get("duration")
    )

    database.session.add(obj)
    database.session.commit()

   
    return render_template("add.html")



@app.route("/show_movies")
def show_blogs():
   all_blog_data = Movie.query.all()

   return render_template("show_movies.html" , data = all_blog_data)


@app.route("/display/<int:number>")
def display(number):
    blog = posts.query.filter(posts.id == number).first()
    if not blog:
        return "blog not found"

    return render_template("display.html" , x = blog)


@app.route("/delete/<int:number>")
def delete(number):
   blog = posts.query.filter(posts.id == number).first()

   if not blog:
       return "blog not found"
    
   database.session.delete(blog)
   database.session.commit()
   return "blog delete succesfully"



@app.route("/update_blog/<int:id>" )
def update_blog(id):
    
    blog = posts.query.filter(posts.id == id).first()
    if not blog:
        return f"blog with id {id} not found,"
    
    if not request.args.get("title") and not request.args.get("description"):
        return render_template("update_blog.html", id = id ) 

    else:  
    
        if request.args.get("title"):
            blog.title = request.args.get("title")

         

        if request.args.get("description"):
            blog.description = request.args.get("description")


    database.session.add(blog)
    database.session.commit()

    return "data updated successfully"  

