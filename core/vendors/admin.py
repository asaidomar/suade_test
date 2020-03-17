#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : admin
# date : 2020-03-16
# project: suade_test
# author : alisaidomar

from django.contrib import admin
from core.vendors import models as vendor_models


@admin.register(vendor_models.Vendor)
class VendorAdmin(admin.ModelAdmin):
    """ Vendor Admin """
    pass


@admin.register(vendor_models.VendorReview)
class ReviewAdmin(admin.ModelAdmin):
    """ Review Admin """
    pass


@admin.register(vendor_models.VendorTag)
class TagAdmin(admin.ModelAdmin):
    """ Tag Admin """
    pass


@admin.register(vendor_models.VendorCategory)
class CategoryAdmin(admin.ModelAdmin):
    """ Category Admin """
    pass
