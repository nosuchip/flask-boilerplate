# -*- coding: utf-8 -*-

import decimal
import json

from datetime import date, datetime

try:
    from config.settings import DATE_FORMAT
except ImportError:
    DATE_FORMAT = '%Y-%m-%d'

try:
    from  config.settings import DATE_TIME_FORMAT
except ImportError:
    DATE_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'



class ExtendedJSONEncoder(json.JSONEncoder):
    """Convers some cases where default JSON encode fails or serialize data
       incorrectly."""

    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        elif isinstance(obj, datetime):
            return obj.strftime(DATE_TIME_FORMAT)
        elif isinstance(obj, date):
            return obj.strftime(DATE_FORMAT)

        return super(PickettJSONEncoder, self).default(obj)
