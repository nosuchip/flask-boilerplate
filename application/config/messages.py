# -*- coding: utf-8 -*-


def get_field_label(key):
    return _field_configs.get(key, {}).get('label', key)


def get_field_description(key):
    return _field_configs.get(key, {}).get('description')


def get_field_label_desc(key):
    return {
        'label': _field_configs.get(key, {}).get('label', key),
        'description': _field_configs.get(key, {}).get('description', key),
    }


def get_field_placeholder(key):
    return _field_configs.get(key, {}).get('placeholder', key)


def get_field_config(key):
    return _field_configs.get(key, {})


def get_message_format(key):
    message = _messages.get(key, '')
    return message


def get_message(key, **kwargs):
    message = _messages.get(key, key)
    return message % kwargs


_field_configs = {
    'SUBMIT': {
        'label': 'Submit',
    }, 'DATE_CREATED': {
        'label': 'Date Created',
        'description': 'Date when record was added initally'
    }, 'DATE_MODIFIED': {
        'label': 'Date Modified',
        'description': 'Date when record was updated last time'
    }, 'EMAIL': {
        'label': 'Email',
        'description': ''
    }, 'PASSWORD': {
        'label': 'Password',
        'description': ''
    }, 'REMEMBER_ME': {
        'label': 'Remember me next time',
        'description': ''
    }
}

_messages = {
    'UNKNOWN_ERROR': 'Unknown error occures. Please reload page and try again.',
    'NO_SUCH_USER': 'No users found accordingly to your criteria.',
    'USER_NOT_AUTHORIZED': 'User is not authorised to perform this action.',
    'USER_NOT_AUTHENTICATED': 'User is not authenticated.',
}
