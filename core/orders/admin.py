#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : admin
# date : 2020-03-17
# project: suade_test
# author : alisaidomar

from django.contrib import admin
from core.orders import models as product_models


class OrderItemAdmin(admin.TabularInline):
    """ Order Item Admin """
    model = product_models.OrderItem
    extra = 1
    min_num = None
    max_num = None


@admin.register(product_models.Order)
class OrderAdmin(admin.ModelAdmin):
    """ Order Admin """
    inlines = [OrderItemAdmin]


@admin.register(product_models.OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    """ Order Admin """
    pass
