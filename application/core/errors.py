# -*- coding: utf-8 -*-

class BaseHttpError(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code

class NotAuthenticatedError(BaseHttpError):
    pass

class NotAuthorizedError(BaseHttpError):
    pass

