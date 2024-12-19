import os
from flask import Flask
from init import db, ma

def create_app():
  app = Flask(__name__)
  # Flask app instance

  print("server started")

  # Retrieve the database URI from the environment variable
  app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("postgres+psycopg2://lms_dev:123456@localhost:5432/lms_db")
  # Default to SQLite for testing if DATABASE_URL is not set

  db.init_app(app)
  ma.init_app(app)

  return app
# application factories^^

import os
from flask import Flask
from init import db, ma

def create_app():
    app = Flask(__name__)

    # Set the database URI
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI")
    # not safe to put straight into file

    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)

    return app
