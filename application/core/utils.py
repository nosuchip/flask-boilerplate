# -*- coding: utf-8 -*-

from datetime import datetime
from flask.ext.security import current_user
import re

def strip_tags(text):
    return re.sub('<[^<]+?>', '', text)

def get_now():
    return datetime.utcnow()

def get_editor():
    return current_user.email if current_user and current_user.is_authenticated() else "system"
