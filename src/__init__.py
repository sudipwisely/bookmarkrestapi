from flask import Flask
import os
from src.auth import auth
from src.bookmarks import bookmarks
from src.database import mysql


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    if test_config is None:
        app.config.from_mapping(SECRET_KEY=os.environ.get("SECRET_KEY"),)
    else:
        app.config.from_mapping(test_config)

    app.config["MYSQL_HOST"] = os.environ.get("MYSQL_HOST")
    app.config["MYSQL_USER"] = os.environ.get("MYSQL_USER")
    app.config["MYSQL_PASSWORD"] = 'sudipsen123'
    app.config["MYSQL_DB"] = os.environ.get("MYSQL_DB")
    mysql.init_app(app)

    app.register_blueprint(auth)
    app.register_blueprint(bookmarks)

    return app
