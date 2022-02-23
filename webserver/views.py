import re
from flask import Blueprint, render_template, request, flash



views = Blueprint("views", __name__)

@views.route("/", methods=["POST", "GET"])
@views.route("/home", methods=["POST", "GET"])
def main():
    if(request == "POST"):
        username = request.form['Username']
        print(username)
    
    return render_template("base.html")
        