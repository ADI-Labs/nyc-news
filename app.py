# -*- coding: utf-8 -*-


from flask import Flask, render_template, request, jsonify
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
        civic_url = "https://www.googleapis.com/civicinfo/v2/representatives?address=" + "New York City" + "&key=AIzaSyAalDN2dXO26te2Soy9gAsOU_wvSlYghVg"
        events_url = "https://www.eventbriteapi.com/v3/events/search/?location.address=New York City&sort_by=date&categories=112&subcategories=12007&token=DPDJZECOID5UA7SDBK25"
        civres = json.loads(requests.get(civic_url).text)
        eventsres = json.loads(requests.get(events_url).text)
        articles = results("default")
        return render_template("index.html", articles = articles, civres = civres, eventsres = eventsres).encode('utf-8')
    else:
        civic_url = "https://www.googleapis.com/civicinfo/v2/representatives?address=" + request.form["location"] + "&key=AIzaSyAalDN2dXO26te2Soy9gAsOU_wvSlYghVg"
        events_url = "https://www.eventbriteapi.com/v3/events/search/?location.address=" + request.form["location"] + "&sort_by=date&categories=112&subcategories=12007&token=DPDJZECOID5UA7SDBK25"
        civres = json.loads(requests.get(civic_url).text)
        eventsres = json.loads(requests.get(events_url).text)
        articles = results(request.form["location"])
        return render_template("index.html", articles = articles, civres = civres, eventsres = eventsres)

@app.errorhandler(404)
def page_not_found(error):
	return "Sorry, this page was not found.", 404

def results(location):
	return data["articles"][location]

if __name__ == "__main__":
	data = json.load(open("data.json"))
	app.run(host="0.0.0.0")