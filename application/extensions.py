# -*- coding: utf-8 -*-

from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from flask.ext.babelex import Babel
babel = Babel()

from flask.ext.mail import Mail
mail = Mail()

from flask.ext.assets import Environment
assets = Environment()

def configure_extensions(app):
    db.init_app(app)
    babel.init_app(app)
    mail.init_app(app)
    assets.init_app(app)
