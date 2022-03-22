from flask import Blueprint, render_template, request
import lib.auth as auth
import lib.lastfm as lastfm
import sys

views = Blueprint("views", __name__)

@views.route("/", methods=["POST", "GET"])
def index():
    config = auth.init()
    lastfm.initCache()
    
    if request.method == "POST":
        username = request.form["Username"]
        config.username=username
        type = request.form["file_type"]
        
        print("Fetching Scrobbles:")
        scrobbles = lastfm.grab(config)
        print("Done!\n")

        if type != 'JSON' or type != 'CSV':
            type = 'ALL'

        lastfm.export(scrobbles, type)

    return render_template("base.html")