# -*- coding: utf-8 -*-

import time
import logging

from functools import wraps

from flask import current_app


def log_execution_time(log_execution_time=True, log_start_time=False, log_end_time=False, logger_name=None):
    """Log method execution time to current application's log or to log specified by `logger_name`

        Usage:

        @log_execution_time(True, True, True, 'performance_logger')
        def method(a, b, *args, **kwargs):
            ....

    """

    def actual_decorator(func):
        @wraps(func)
        def decorated_view(*func_args, **func_kwargs):
            start_time = time.time()

            logger = logging.getLogger(logger_name) if logger_name else current_app.logger

            if log_start_time:
                logger.info('Function "{}" started with args "{}", kwargs "{}"'.format(
                    func.__name__, func_args, func_kwargs
                ))

            result = func(*func_args, **func_kwargs)
            end_time = time.time()

            if log_end_time:
                logger.info('Function "{}" finished with args "{}", kwargs "{}"'.format(
                    func.__name__, func_args, func_kwargs
                ))

            if log_execution_time:
                logger.info('function "{}" with args "{}", kwargs "{}" executed for {} seconds'.format(
                    func.__name__, func_args, func_kwargs, int(end_time - start_time)
                ))

            return result
        return decorated_view

    return actual_decorator
