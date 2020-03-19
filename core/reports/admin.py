#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : admin
# date : 2020-03-19
# project: suade_test
# author : alisaidomar

from django.contrib import admin
from core.reports import models as report_models


@admin.register(report_models.Report)
class OrderAdmin(admin.ModelAdmin):
    """ Report Admin """
    pass
