from flask import Blueprint, render_template


#Blueprints need to be stored at __init__.py file
views = Blueprint("views", __name__)

#Route where this will be stored
@views.route('/')

def index():
    return render_template("index.html")

