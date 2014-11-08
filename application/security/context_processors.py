# -*- coding: utf-8 -*-

from application.config.app import PAGES

def init_context_processors(security):
    def get_page(processor, **kwargs):
        params = PAGES.get(processor, {}).get('params', {})
        params.update(**kwargs)
        return params


    #@security.login_context_processor
    #def login_context_processor():
    #    return get_page('login', message='PUT PARAMETERS FOR LOGIN PAGE HERE')

    #@security.register_context_processor
    #def register_context_processor():
    #    return get_page('register', message='PUT PARAMETERS FOR LOGIN PAGE HERE')
