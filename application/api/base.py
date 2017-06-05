# -*- coding: utf-8 -*-

import json


def response_json(self, success=True, message=None, data=None, code=200, mimetype='application/json'):
    """Make API JSON response tuple `json, code, mimetype` like: {'success': False, 'message': '', 'data': {}}
    """
    data = {'success': success}

    if message is not None:
        data['message'] = message
    if data is not None:
        data['data'] = data

    # Flask-like response, to response real `Response` object use `flask.Response(*response_json(...))`
    return (
        json.dumps(data, cls=json_encoder.PickettJSONEncoder),
        code,
        mimetype
    )


def response_ok(self, message='', data=None):
    """API call successful, result ready and returned"""
    return self.response_json(success=True, message=message, data=data)


def response_fail(self, message='', data=None):
    """API call unsuccessful, message should be provided"""
    return self.response_json(success=False, message=message, data=data)


def response_error(self, message='', data=None):
    """API call failed and cannot be processed"""
    return self.response_json(success=False, message=message, data=data, code=500)


def response_not_found(self, message='', data=None):
    """API call failed, resource not found"""
    return self.response_json(success=False, message=message, data=data, code=404)


def response_forbidden(self, message='', data=None):
    """API call failed, access denied"""
    return self.response_json(success=False, message=message, data=data, code=401)
