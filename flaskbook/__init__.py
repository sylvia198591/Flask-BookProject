from flask import Flask
from flask_restplus import Api,Resource
from flaskbook.db import initialize_db
from flask_pymongo import PyMongo
from werkzeug.utils import cached_property
from flaskbook.book.routes import initialize_routes

def create_app(config_object='flaskbook.settings'):
    app = Flask(__name__)
    app.config.from_object(config_object)
    api = Api(app)
    initialize_db(app)
    # app.register_blueprint(movies)
    initialize_routes(api)
    return app