# -*- coding: utf-8 -*-

import os

DATABASE_URI = os.getenv('DATABASE_URI')
SQLALCHEMY_ENGINE_PARAMS = {
    'echo': bool(os.getenv('SQLALCHEMY_ECHO', False)),
    'pool_size': 100,
    'pool_recycle': 280,
    'pool_timeout': 20
}

SQLALCHEMY_SESSION_PARAMS = {
    'autoflush': False
}
