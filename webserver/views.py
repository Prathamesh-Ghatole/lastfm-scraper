from flask import Blueprint, render_template, request, flash
import sys

views = Blueprint("views", __name__)

@views.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        username = request.form["Username"]
        type = request.form["file_type"]
        print(username)
        print(type)
    return render_template("base.html")
        