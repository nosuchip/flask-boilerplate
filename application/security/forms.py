# -*- coding: utf-8 -*-
import flask.ext.security.forms as forms
from wtforms import validators, StringField, PasswordField
from flask.ext.wtf import Form
from application.core.filters import strip, lower
from application.config.messages import get_field_label


class RegisterInfoMixin():
    first_name = forms.TextField('First Name', filters=[strip],
        validators=[validators.Optional(), validators.Length(min=3, max=128)])
    last_name = forms.TextField('Last Name', filters=[strip],
        validators=[validators.Optional(), validators.Length(min=3, max=128)])


class ConfirmRegisterForm(forms.ConfirmRegisterForm, forms.PasswordConfirmFormMixin, RegisterInfoMixin):
    email = forms.TextField(
        forms.get_form_field_label('email'),
        validators=[forms.email_required, forms.email_validator, forms.unique_user_email],
        filters=[strip, lower]
    )


class RegisterForm(ConfirmRegisterForm, forms.PasswordConfirmFormMixin):
    pass


class ProfileForm(Form):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.password.data = '********'

    first_name = StringField(get_field_label('FIRST_NAME'), validators=[validators.Required()])
    last_name = StringField(get_field_label('LAST_NAME'), validators=[validators.Required()])
    email = StringField(get_field_label('EMAIL'), validators=[validators.Required(), validators.Email()])
    password = PasswordField(get_field_label('PASSWORD'), validators=[validators.Required()])
