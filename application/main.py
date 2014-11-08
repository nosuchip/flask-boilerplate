# -*- coding: utf-8 -*-

import os
from flask import Flask
from application.extensions import babel, mail, db
from application.routes import configure_routes
from application.security import init_security
from application.admin import init_admin


def init(name):
    app = Flask(name)

    configure_app(app)
    init_extensions(app)
    init_signals(app)
    init_blueprints(app)
    configure_routes(app)
    init_admin(app)

    return app


def configure_app(app):
    app.config.from_object('application.config.flask')
    app.config.from_object('application.config.app')
    app.config.from_envvar('APP_SETTINGS', silent=app.config['DEBUG'])

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('APP_DB_URI', None)


def init_extensions(app):
    babel.init_app(app)
    mail.init_app(app)
    db.init_app(app)
    assets.init_app(app)
    init_security(app)


def init_signals(app):
    try:
        from application.signals import connect
        connect(app)
    except ImportError:
        pass


def init_blueprints(app):
    #Views

    #from application.security.views import module as user_view
    #app.register_blueprint(user_view, url_prefix='')

    #Services
    from application.service.comment import module as comment_view
    app.register_blueprint(comment_view, url_prefix='/service/comment')


app = init(__name__)
