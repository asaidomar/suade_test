#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : models
# date : 2020-03-17
# project: suade_test
# author : alisaidomar
from collections import defaultdict
from functools import reduce
from typing import List, Dict

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Order(models.Model):
    """ Order model """

    AMOUNT_KEYS = ("full_price_amount",
                   "discounted_amount",
                   "vat_amount",
                   "total_amount")
    created_at = models.DateTimeField(
        _('Order creation date'))
    customer = models.ForeignKey('members.Member', on_delete=models.DO_NOTHING)
    vendor = models.ForeignKey('vendors.Vendor', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.customer}/{self.created_at}"

    def get_total(self, *dict_prices: Dict):
        """ Get total against current order.
        Compute a dict according to keys `total_amount` """
        return {k: sum([d[k] for d in dict_prices]) for k in self.AMOUNT_KEYS}

    @property
    def items_price(self) -> Dict:
        """ Return order price """
        result = {}
        items = self.items.prefetch_related("product__vendor", "discount")
        price = self.get_price(items)
        result["items"] = price
        result["total_amount"] = reduce(self.get_total, price.values())
        return result

    @staticmethod
    def apply_rate(amount: float, rate: float, positive=True):
        """ Apply rate to amount"""
        if positive:
            return amount * (1 + rate)
        return amount * (1 - rate)

    def get_price(self, items: List['OrderItem'] = None) -> Dict:
        """ Return dict of price per item

        Vat amount, discount amount and total
        """
        result = defaultdict()
        for item in (items or self.items.all()):
            excl_taxes = item.quantity * item.product.price
            incl_taxes = self.apply_rate(
                excl_taxes, item.product.vat_rate)
            discounted_amount = float(item.discount.rate) * float(incl_taxes)
            try:
                promotion_id = item.product.promotion.promotion.id
            except Exception as error:  # noqa
                promotion_id = 0
            result[item.product.code] = {
                "promotion": promotion_id,
                "description": item.product.description,
                "full_price_amount": incl_taxes,
                "discounted_amount": discounted_amount,
                "vat_amount": excl_taxes * item.product.vat_rate,
                "product_vat_rate": item.product.vat_rate,
                "total_amount": incl_taxes - discounted_amount
            }
        return result


class OrderItem(models.Model):
    """ Order Item """
    order = models.ForeignKey(
        'Order', on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(
        'products.Product', on_delete=models.DO_NOTHING)
    discount = models.ForeignKey(
        'promotions.Discount', on_delete=models.DO_NOTHING,
        blank=True, null=True)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product}/{self.order}"
