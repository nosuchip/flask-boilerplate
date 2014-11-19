# -*- coding: utf-8 -*-

import os, mimetypes
from flask import redirect, render_template, send_from_directory, url_for, redirect
from application.config.app import PAGES
from flask.ext.security import login_required

mimetypes.add_type('image/png', '.png', True)

def configure_routes(app):
    def configured_route(name):
        page = PAGES[name]
        page['params'].update({'some': 'value'})
        return render_template(page['template'], **page['params'])

    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(os.path.join(app.root_path, 'static', 'img'),
            'favicon.ico', mimetype='image/vnd.microsoft.icon')

    @app.errorhandler(404)
    def page_error_404(error):
        return configured_route('error_404')

    @app.errorhandler(500)
    def page_error_500(error):
        return "Error 500:", error
        #configured_route('error_500')


    #This is just an example for very simple routing
    #aimed to provide semi-static content without complex data binding
    #I.e. most of data can be retrieved from config
    #All other routes should be added via Blueprints
    @app.route('/')
    def home():
        return configured_route('home')

    @app.route('/about/')
    def about():
        return configured_route('about')
