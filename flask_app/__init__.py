import logging
from logging.config import dictConfig

from config import LOGGING_CONFIG
from flask import Flask

dictConfig(LOGGING_CONFIG)


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')
    app.config.from_pyfile('config.py')

    # register blueprints
    # from flask_app.views import blueprint
    # app.register_blueprint(blueprint)

    # register db
    from flask_app.database import db
    db.init_app(app)

    # register serializer
    from flask_app.serialize import ma
    ma.init_app(app)

    # register resources
    from flask_restful import Api

    from flask_app.resources import ENDPOINT, ChineseWordResource
    api = Api(app)
    api.add_resource(ChineseWordResource, ENDPOINT)

    return app
