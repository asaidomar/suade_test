#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : admin
# date : 2020-03-17
# project: suade_test
# author : alisaidomar

from django.contrib import admin
from core.products import models as product_models


@admin.register(product_models.Product)
class ProductAdmin(admin.ModelAdmin):
    """ Product Admin """
    pass
