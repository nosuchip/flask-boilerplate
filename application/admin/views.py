# -*- coding: utf-8 -*-
from flask.ext.admin.contrib.sqla import ModelView
from application.config.app import ADMIN_CONFIG
from flask.ext.security import current_user


class AdminModelView(ModelView):
    page_size = ADMIN_CONFIG['page_size']

    @property
    def can_create(self):
        return current_user.has_role('admin')

    @property
    def can_edit(self):
        return current_user.has_role('admin')

    @property
    def can_delete(self):
        return current_user.has_role('admin')

    def is_accessible(self):
        return has_admin_role()


#class AdminSampleView(AdminModelView):
#    column_list = (...)
#    column_filters = [...]
#    column_searchable_list = (...)


def add_admin_views(admin):
    #admin.add_view(AdminSampleView(SampleModel, 'Sample', category='Sample'))

    admin.add_link(MenuLink(name='Portal', url='/'))
    admin.add_link(MenuLink(name='Log Out', url='/logout/'))
