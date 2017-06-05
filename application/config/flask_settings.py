# -*- coding: utf-8 -*-

import os

# Here stored settings related to Flask instance and extensions
# Normally this file should not be imported anywhere

SECRET_KEY = 'd+/6n~G@]gt.&j"%pku?5<7?GcP;?fDn-3)%cg~g&NN%3LmhH#fmW!A(\4a8Vr%ff4%ZHMk&(J(54q_'
DEBUG = os.getenv('ENVIRONMENT') != 'production'
