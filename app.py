from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("hello.html")

@app.route("/news")
def news():
    return render_template("news.html")

@app.route("/name")
def name():
    return "Sanford"


@app.route("/website")
def website():
    return "https://adicu.com/webdev"


@app.route("/search", methods=["GET", "POST"])
def search():
    if (request.method == "POST"):
        url = "https://api.github.com/search/repositories?q=" + request.form["user_search"]
        response_dict = requests.get(url).json()
        return render_template("results.html", api_data=response_dict)
    else:
        return render_template("search.html")


@app.route("/add/<x>/<y>")
def add(x, y):
    return str(int(x) + int(y))


@app.errorhandler(404)
def page_not_found(error):
    return "Sorry, this page was not found.", 404


def parse_response(dictionary):
    received_dict = dictionary
    del received_dict["incomplete_results"]
    for repo in received_dict["items"]:
        for key in list(repo.keys()):
            if (key != "name"
                and key != "owner"
                and key != "html_url"
                and key != "description"):
                del repo[key]
            elif (key == "owner"):
                for subkey in list(repo["owner"]):
                    if (subkey != "login"
                        and subkey != "avatar_url"
                        and subkey != "html_url"):
                        del repo["owner"][subkey]
    return received_dict


if __name__ == "__main__":
    app.run(host="localhost")

    # python3.5 "/Users/Sanford/Google Drive/Code/Python/HelloWorldFlask/app.py"
