#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : models
# date : 2020-03-17
# project: suade_test
# author : alisaidomar

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Order(models.Model):
    """ Order model """
    created_at = models.DateTimeField(
        _('Order creation date'), auto_now_add=True)
    customer = models.ForeignKey('members.Member', on_delete=models.DO_NOTHING)
    vendor = models.ForeignKey('vendors.Vendor', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.customer}/{self.created_at}"


class OrderItem(models.Model):
    """ Order Item """
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey(
        'products.Product', on_delete=models.DO_NOTHING)
    discount = models.ForeignKey(
        'promotions.Discount', on_delete=models.DO_NOTHING,
        blank=True, null=True)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product}/{self.order}"
