#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : __init__.py
# date : 2020-03-16-15-23
# project: suade_test
# author : alisaidomar

from .api import urlpatterns as api_urlpatterns
from .root import urlpatterns as root_urlpatterns

urlpatterns = api_urlpatterns + root_urlpatterns
