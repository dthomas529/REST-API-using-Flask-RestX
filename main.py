from flask import Flask
from .extensions import db, api
from .resources import ns

def create_app(): #create app function that return app object
  app = Flask(__name__)

  app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
  
  api.init_app(app)
  db.init_app(app)

  api.add_namespace(ns)
  
  return app
  
