
from flask import Flask, render_template
from firebase import firebase

app = Flask(__name__)
firebase = firebase.FirebaseApplication("https://labs-2c94e.firebaseio.com", None)

@app.route("/index.html", methods = ["GET", "POST"])
@app.route("/index", methods = ["GET", "POST"])
@app.route("/", methods = ["GET", "POST"])
@app.route("", methods = ["GET", "POST"])
def homepage():
    if request.method == "GET":
        return render_template("index.html")
    else:
        return render_template("index.html")

@app.errorhandler(404)
def page_not_found(error):
	return "Sorry, this page was not found.", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0")