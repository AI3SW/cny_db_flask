import logging
from logging.config import dictConfig

from config import LOGGING_CONFIG
from flask import Flask

dictConfig(LOGGING_CONFIG)


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')

    # register blueprints
    from flask_app.views import blueprint
    app.register_blueprint(blueprint)

    return app
