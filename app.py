# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
import requests, json
from firebase import firebase
import itertools

app = Flask(__name__)
firebase = firebase.FirebaseApplication("https://labs-2c94e.firebaseio.com", None)

@app.route("/index.html", methods = ["GET", "POST"])
@app.route("/index", methods = ["GET", "POST"])
@app.route("/", methods = ["GET", "POST"])
def homepage():
    if request.method == "GET":
    	url = "https://www.googleapis.com/civicinfo/v2/representatives?address=10027&key=AIzaSyAalDN2dXO26te2Soy9gAsOU_wvSlYghVg"
    	res = requests.get(url).json()
    	articles = results("default")
    	return render_template("index.html", articles = articles, reps = res)
    else:
    	url = "https://www.googleapis.com/civicinfo/v2/representatives?address=10027&key=AIzaSyAalDN2dXO26te2Soy9gAsOU_wvSlYghVg"
    	res = requests.get(url).json()
    	articles = results(request.form["location"])
    	return render_template("index.html", articles = articles, reps = res)

@app.errorhandler(404)
def page_not_found(error):
	return "Sorry, this page was not found.", 404

def results(location):
	return data["articles"][location]

if __name__ == "__main__":
	data = json.load(open("data.json"))
	app.run(host="0.0.0.0")