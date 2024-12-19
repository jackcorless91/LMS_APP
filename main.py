import os 
from flask import Flask
from init import db, ma


def create_app():
  app = Flask(__name__)
  #  flask app instance

  app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI")
  # insecure to write directly into file

  db.init_app(app)
  ma.init_app(app)

  return app
# application factories^^