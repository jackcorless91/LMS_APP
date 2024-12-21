import os
from flask import Flask
from init import db, ma
from controllers.cli_controller import db_commands
from controllers.student_controller import students_bp


def create_app():
    app = Flask(__name__)

    # Set the database URI
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI")
    # not safe to put straight into file

    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)

    app.register_blueprint(db_commands)
    app.register_blueprint(students_bp)

    return app
