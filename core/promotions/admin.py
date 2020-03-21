#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : admin
# date : 2020-03-16
# project: suade_test
# author : alisaidomar

from django.contrib import admin
from core.promotions import models as promotion_models


@admin.register(promotion_models.Discount)
class DiscountAdmin(admin.ModelAdmin):
    """ Discount Admin """
    pass


@admin.register(promotion_models.Promotion)
class PromotionAdmin(admin.ModelAdmin):
    """ Discount Admin """
    pass


@admin.register(promotion_models.ProductPromotion)
class ProductPromotionAdmin(admin.ModelAdmin):
    """ Discount Admin """
    pass
