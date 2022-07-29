from email import message
from flask import Blueprint, render_template, request, send_file, redirect, url_for, flash
import lib.auth as auth
import lib.lastfm as lastfm
import sys

views = Blueprint("views", __name__)
dictt ={
    "username": None,
    "type": None
}

@views.route("/", methods=["POST", "GET"])
def index():
    config = auth.init()
    lastfm.initCache()
    flash("Click on ")
    
    if request.method == "POST":
        dictt["username"] = request.form["Username"]
        config.username=dictt["username"]
        dictt["type"] = request.form["file_type"]
        type = dictt["type"]
                
        return render_template("base.html", config = config, type = type)

    return render_template("base.html")


@views.route("/download/<type>")
def download(type):
    config = auth.init()
    lastfm.initCache()
    print("Fetching Scrobbles:")
    scrobbles = lastfm.grab(config)
    print("Done!\n")

    # if type != 'JSON' or type != 'CSV':
    #     type = 'ALL'
    lastfm.export(scrobbles, type)

    print(dictt["type"])
    if dictt["type"] == 'JSON':
        path = "../exports/export.json"
    elif dictt["type"] == "CSV":
        path = "../exports/export.csv"
    return send_file(path, as_attachment = True)

@views.route("/contact")
def contact():
    return render_template("contact.html")