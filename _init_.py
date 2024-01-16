from flask import Flask
from .extensions import db, api
from .resources import ns

def create_app(): #create app function that return app object
  app = Flask(__name__) #creates an instance of the Flask web

  app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3" #database configuration
  
  api.init_app(app) #a method call that initializes the API with the Flask application (app)
  db.init_app(app) ##a method call that initializes the database with the Flask application (app)

  api.add_namespace(ns) #to organize resources and route them based on a common path or URL prefix.
  
  return app # return the app