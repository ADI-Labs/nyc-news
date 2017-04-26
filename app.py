# -*- coding: utf-8 -*-
from flask import Flask, render_template, redirect, request, session, jsonify
import requests, json
import itertools
import pyrebase

app = Flask(__name__)
app.secret_key = "4bc58f6f5e45081f30e0da846ad3560dc347798dbc4373b9"

config = {
    "apiKey" : "AIzaSyBeIOzvNIlY90DRAj8HhXNLL5aCLhNylB4",
    "authDomain" : "labs-2c94e.firebaseapp.com",
    "databaseURL" : "https://labs-2c94e.firebaseio.com",
    "projectId" : "labs-2c94e",
    "storageBucket" : "labs-2c94e.appspot.com",
    "messagingSenderId" : "615805281183"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

@app.route("/index.html", methods = ["GET"])
@app.route("/index", methods = ["GET"])
@app.route("/", methods = ["GET"])
def homepage():
    if "user" in session:
        user = auth.refresh(session['user']['refreshToken'])
        session['user'] = user
        civic_url = "https://www.googleapis.com/civicinfo/v2/representatives?address=" + "New York City" + "&key=AIzaSyAalDN2dXO26te2Soy9gAsOU_wvSlYghVg"
        events_url = "https://www.eventbriteapi.com/v3/events/search/?location.address=" + "New York City" + "&sort_by=date&categories=112&subcategories=12007&token=DPDJZECOID5UA7SDBK25"
        civres = json.loads(requests.get(civic_url).text)
        eventsres = json.loads(requests.get(events_url).text)
        articles = results("default")
    else:
        civic_url = "https://www.googleapis.com/civicinfo/v2/representatives?address=" + "New York City" + "&key=AIzaSyAalDN2dXO26te2Soy9gAsOU_wvSlYghVg"
        events_url = "https://www.eventbriteapi.com/v3/events/search/?location.address=" + "New York City" + "&sort_by=date&categories=112&subcategories=12007&token=DPDJZECOID5UA7SDBK25"
        civres = json.loads(requests.get(civic_url).text)
        eventsres = json.loads(requests.get(events_url).text)
        articles = results("default")
    return render_template("index.html", civres = civres, eventsres = eventsres, articles = articles)

@app.route("/index.html", methods = ["POST"])
def search_neighborhood():
    civic_url = "https://www.googleapis.com/civicinfo/v2/representatives?address=" + request.form['location'] + "&key=AIzaSyAalDN2dXO26te2Soy9gAsOU_wvSlYghVg"
    events_url = "https://www.eventbriteapi.com/v3/events/search/?location.address=" + request.form['location'] + "&sort_by=date&categories=112&subcategories=12007&token=DPDJZECOID5UA7SDBK25"
    civres = json.loads(requests.get(civic_url).text)
    eventsres = json.loads(requests.get(events_url).text)
    articles = results(request.form['location'])
    return render_template("index.html", civres = civres, eventsres = eventsres, articles = articles)

@app.route("/sign-out", methods = ["POST"])
def sign_out():
    del session['user']
    return redirect("index.html")

@app.route("/preferences.html", methods = ["GET"])
@app.route("/preferences", methods = ["GET"])
def preferences_page():
    user = auth.refresh(session['user']['refreshToken'])
    session['user'] = user
    default_neighborhood = "Placeholder"
    return render_template("preferences.html", default_neighborhood = default_neighborhood)

@app.route("/preferences", methods = ["POST"])
def preferences():
    return redirect("preferences.html")

@app.route("/set-neighborhood", methods = ["POST"])
def set_neighborhood():
    user = auth.refresh(session['user']['refreshToken'])
    session['user'] = user
    db.child("users").child(session['user']['userId']).set({"neighborhood": request.form['location']}, session['user']['idToken'])
    return redirect("preferences.html")

@app.route("/sign-in", methods = ["POST"])
def sign_in():
    return render_template("sign-in.html")

@app.route("/sign-in-form", methods = ["POST"])
def sign_in_form():
    email = request.form['email']
    password = request.form['password']
    user = auth.sign_in_with_email_and_password(email, password)
    if user != None:
        session['user'] = user
        return redirect("index.html")
    else:
        return redirect("sign-in")

@app.route("/sign-up", methods = ["POST"])
def sign_up():
    return render_template("sign-up.html")

@app.route("/sign-up-form", methods = ["POST"])
def sign_up_form():
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form["confirm-password"]
    if password == confirm_password:
        auth.create_user_with_email_and_password(email, password)
        user = auth.sign_in_with_email_and_password(email, password)
        session['user'] = user
        db.child("users").child(session['user']['localId']).set({"neighborhood": "No neighborhood choosen"}, session['user']['idToken'])
        return redirect("index.html")
    else:
        return redirect("/sign-up")

@app.errorhandler(404)
def page_not_found(error):
	return "Sorry, this page was not found.", 404

def results(location):
	return data['articles'][location]

if __name__ == "__main__":
	data = json.load(open("data.json"))
	app.run(host="0.0.0.0")