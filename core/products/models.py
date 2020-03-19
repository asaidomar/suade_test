#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : models
# date : 2020-03-17
# project: suade_test
# author : alisaidomar

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Product(models.Model):
    """ Product model """
    creation_date = models.DateField(
        _("Product creation date"), auto_now_add=True)
    update_date = models.DateField(
        _("Product update date"), auto_now=True)
    code = models.CharField(
        _("Product Code"), max_length=255, unique=True)
    brand = models.CharField(
        _("Product Brand"), max_length=255, blank=True, null=True)
    description = models.CharField(
        _("Product description"), max_length=255)
    price = models.PositiveIntegerField(_("Product price, excl. taxes"))
    vendor = models.ForeignKey(
        "vendors.Vendor", on_delete=models.DO_NOTHING)
    currency = models.CharField(_("Product Currency"), max_length=15)

    def __str__(self):
        return f"{self.description}"
