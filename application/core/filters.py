# -*- coding: utf-8 -*-

from flask import current_app

strip = lambda s: s.strip() if s is not None else None
lower = lambda s: s.lower() if s is not None else None

def app_config_item(name):
    return current_app.config[name]
