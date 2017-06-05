# -*- coding: utf-8 -*-

from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from application.config import db_settings

database_engine = create_engine(db_settings.DATABASE_URI, **db_settings.SQLALCHEMY_ENGINE_PARAMS)
session_factory = sessionmaker(bind=database_engine, **db_settings.SQLALCHEMY_SESSION_PARAMS)
session = session_factory()


def create_scoped_session():
    return scoped_session(session_factory)
