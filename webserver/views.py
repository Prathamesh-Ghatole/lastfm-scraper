from flask import Blueprint, render_template, request, send_file, redirect, url_for, flash
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
        
        return redirect(url_for("views.download"))

    return render_template("base.html")


@views.route("/download")
def download():
    path = "..\exports\export.json"

    if type == 'JSON':
        path = "..\exports\export.json"
    if type == "CSV":
        path = "..\exports\export.csv"
          
    return send_file(path, as_attachment = True, )
