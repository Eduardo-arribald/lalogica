from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path



#This module serves to store website folder as a python module

def create_app(): 
    app = Flask(__name__)

    #Secret key helps to secure the website
    app.config['SECRET_KEY'] = "asldkfjaslvmp"

    #Here we tell where our sqlite database is stored
    
    #Import blueprints
    from .views import views
    from .optimizer import optimizer


    #Prefix here serves to prefix the one defined at views.py file.
    #If anything is added to this url_prefix, it will be before defined prefix at views.py file.
    app.register_blueprint(views, url_prefix = "/")     
    app.register_blueprint(optimizer, url_prefix = "/")


    return app