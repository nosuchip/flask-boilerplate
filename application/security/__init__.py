# -*- coding: utf-8 -*-
from flask.ext.security import Security, SQLAlchemyUserDatastore
from application.extensions import db
from models import User, Role
from application.security.forms import (
    ConfirmRegisterForm,
    RegisterForm,
    LoginForm
)

def init_security(app):
    security = Security(
        app,
        SQLAlchemyUserDatastore(db, User, Role),
        confirm_register_form=ConfirmRegisterForm,
        login_form=LoginForm
    )

    from application.security.context_processors import init_context_processors
    init_context_processors(security)
