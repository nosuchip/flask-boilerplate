# -*- coding: utf-8 -*-

from flask import Flask

from application.routes import configure_routes
from application.common import filters
from application.common import json_enc


def init(name):
    app = Flask(name)

    configure_app(app)
    configure_extensions(app)
    configure_routes(app)

    return app


def configure_app(app):
    app.config.from_object('application.config.flask_settings')

    app.jinja_env.globals['url_for_static'] = filters.url_for_static

    # Define useful filters
    app.jinja_env.filters['app_settings_item'] = filters.app_settings_item
    app.jinja_env.filters['to_json'] = filters.to_json
    app.jinja_env.filters['date'] = filters.as_date

    app.json_encoder = json_enc.ExtendedJSONEncoder


def configure_extensions(app):
    pass


app = init(__name__)
