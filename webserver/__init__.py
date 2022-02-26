from flask import Flask, render_template, url_for
app = Flask(__name__)
app.config['SECRET_KE']= "SuperSecure"

from .views import views
app.register_blueprint(views, url_prefix="/")



