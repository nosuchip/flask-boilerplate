# -*- coding: utf-8 -*-


FIELDS = {
    'EMAIL': {
        'label': 'Email',
        'description': 'Email field used as login',
        'placeholder': 'E-Mail'
    }
}

MESSAGES = {
    'UNKNOWN_ERROR': 'Unknown error occures. Please reload page and try again.',
    'NO_SUCH_USER': 'No users found accordingly to your criteria.',
    'USER_NOT_AUTHORIZED': 'User is not authorised to perform this action.',
    'USER_NOT_AUTHENTICATED': 'User is not authenticated.',
}



def _safe_format(template, **kwargs):
    context = dict((key, value) for key, value in kwargs.items() if '{{{k}}}'.format(k=key) in template)
    return template.format(**context)


def get_message(key, source=MESSAGES, **kwargs):
    template = source.get(key, None)
    return key if not template else _safe_format(template, **kwargs)


def get_field_label(key, source=FIELDS, required=False, **kwargs):
    template = source.get(key, {}).get('label')

    if not template:
        return key

    value = _safe_format(template, **kwargs)

    if required:
        value += ' *'

    return value


def get_field_placeholder(key, source=FIELDS, **kwargs):
    template = source.get(key, {}).get('placeholder')
    return key if not template else _safe_format(template, **kwargs)


def get_field_description(key, source=FIELDS, **kwargs):
    template = source.get(key, {}).get('description')
    return key if not template else _safe_format(template, **kwargs)
