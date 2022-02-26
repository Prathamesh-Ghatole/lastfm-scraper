from flask import Blueprint, render_template, request
import lib.auth as auth
import lib.lastfm as lastfm
import sys

views = Blueprint("views", __name__)

def demo(username):
    config = auth.initialize()
    lastfm.initCache()
    response = lastfm.getReq(key=config.getKey(), useragent=config.useragent, user=username, method='artist.getInfo', load={'artist':'Taylor Swift'})
    return response.json()['artist']

@views.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        username = request.form["Username"]
        type = request.form["file_type"]
        print(demo(username=username))
        print(username)
        print(type)
    return render_template("base.html")
        