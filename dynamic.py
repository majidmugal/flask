from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> home page </h1>"

@app.route("/<xyz>/<pqr>")
def xyz_test(xyz , pqr):
    return f"value of var is {xyz}, {pqr}"

@app.route("/profile/<xyz>")
def about(xyz):
    return f"my instagram id is {xyz}"

@app.route("/contact")
def contact():
    return "Contact Us"

@app.route("/services")
def services():
    return "Our Services"  

@app.route("/test_int/<int:a>")
def test_int(a):
    return str(a)


@app.route("/test_float/<float:a>")
def test_float(a):
    return str(a)




@app.route("/test_path/<path:a>")
def test_path(a):
    return str(a)