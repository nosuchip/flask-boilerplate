# -*- coding: utf-8 -*-
from flask.ext.admin import Admin
from application.admin.views import add_admin_views

def init_admin(app):
    admin = Admin(app, name=APP_NAME, index_view=AdminDashboardView(ADMIN_INDEX_TITLE))

    add_admin_views(admin)
