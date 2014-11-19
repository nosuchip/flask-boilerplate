APP_NAME = 'Flask Boilerplate'

PAGES = {
    'home' : {
        'template': 'home.html',
        'params': {
            'page_title': 'Home',
            'page': 'home'
        }
    },
    'about' : {
        'template': 'about.html',
        'params': {
            'page_title': 'About',
            'page': 'about'
        }
    },
    'error_404': {
        'template': 'error.html',
        'params': {
            'page_title': 'Error 404: Not Found',
            'error_header': 'Page not found',
            'error_text': 'The requested URL was not found on this server.'
        }
    },
    'error_500': {
        'template': 'error.html',
        'params': {
            'page_title': 'Error 500: Internal Server Error',
            'error_header': 'Internal server error',
            'error_text': 'An error occurred in the application. Please try again in a few moments.'
        }
    },
    'login': {
        'params': {
            'page_title': 'Sign in',
            'page': 'login'
        }
    },
    'register': {
        'params': {
            'page_title': 'Sign up',
            'page': 'register'
        }
    },
}

ADMIN_CONFIG = {
    'page_size': 15
}
