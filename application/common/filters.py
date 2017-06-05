# -*- coding: utf-8 -*-


import json
from datetime import date, datetime
from flask import current_app, url_for
from application.config import settings

try:
    from application.config.settings import DATE_FORMAT
except ImportError:
    DATE_FORMAT = '%Y-%m-%d'


def app_settings_item(key, default=None):
    """
    Jinja filter to retrieve data from settings module (`config.settings`).
    Acceptable input is:
    - dot-separated hierarchical key, value will be retrieved
        recursively until last one is caught. None returns if an exception occurred
        or False-evaluatable value is received
    - Iterable of keys (joined by dot will returns the same string as
        in option 1). Value will be retrieved recursively.
    """

    def _get_setting_value(scope, keys):
        try:
            for one_key in keys:
                if isinstance(scope, dict):
                    scope = scope.get(one_key, None)
                else:
                    scope = getattr(scope, one_key, None)

                if not scope:
                    return None

            return scope
        except Exception as ex:
            current_app.logger.debug(
                'get_from_settings: error occurred: {}'.format(str(ex))
            )
            return None

    if isinstance(key, str):
        return _get_setting_value(settings, key.split('.'))
    elif isinstance(key, (tuple, list)):
        return _get_setting_value(key)

    return default


def to_json(context, default=None):
    """Convert Python object to JSON"""
    return json.dumps(context) if context is not None else default


def url_for_static(*args, **kwargs):
    """Generate url for static resources in short way similar to :func:`flask.url_for`"""
    if 'filename' not in kwargs and args:
        kwargs['filename'] = args[0]
        args = tuple(args[1:])

    return url_for('static', *args, **kwargs)


def percents(value, decimal_values=0):
    """Format string as percents

    :param decimal_values: number of digits after decimal comma
    """
    fmt = '{0:.' + str(decimal_values) + 'f}'
    return fmt.format((value or 0) * 100)


def currency(value, currency_prefix='$', denominator=1, decimal_values=0, default=0):
    """Format string as percents

    :param currency_prefix: prefix to be added before formatted value
    :param denominator: used to convert long numbers to human readable format like `1k` or `5m`
    :param decimal_values: number of digits after decimal comma
    :param default: default value returned if  `value` cannot be converted to float or formatted
    """
    denominator_mappings = {
        1000: 'k',
        1000000: 'm',
        1000000000: 'b'
    }

    if denominator not in denominator_mappings:
        denominator, postfix = 1, ''
    else:
        denominator, postfix = denominator, denominator_mappings[denominator]

    try:
        value = float(value) / denominator

        fmt = '{0:,.' + str(decimal_values) + 'f}'

        if currency_prefix:
            fmt = str(currency_prefix) + fmt

        if denominator > 1:
            fmt = fmt + ' ' + postfix

        return fmt.format(value)
    except:
        return default


def count(query_object):
    """Return count of passed object `query_object`

    :param query_object: could be either SQLAlchemy :class:`~sqlalchemy.InstrumentedList` or iterable
    """

    result = getattr(query_object, 'count', None)

    if result is None and hasattr(query_object, '__len__'):
        result = len(query_object)

    if callable(result):
        result = result()

    return result


def as_date(value):
    return value.strftime(DATE_FORMAT) if type(value) in [date, datetime] else value
