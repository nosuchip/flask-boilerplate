# -*- coding: utf-8 -*-
from application.config.app import APP_NAME
from flask.ext.admin import Admin
from application.admin.views import add_admin_views

def init_admin(app):
    admin = Admin(app, name=APP_NAME)

    add_admin_views(admin)
