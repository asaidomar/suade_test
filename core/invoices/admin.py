#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : admin
# date : 2020-03-18
# project: suade_test
# author : alisaidomar

from django.contrib import admin
from core.invoices import models as invoice_models


@admin.register(invoice_models.Commission)
class CommissionAdmin(admin.ModelAdmin):
    """ Discount Admin """
    pass
