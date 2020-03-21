#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : models
# date : 2020-03-17
# project: suade_test
# author : alisaidomar
from collections import defaultdict
from datetime import datetime
from functools import reduce
from typing import List, Dict

from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.invoices.models import Commission
from core.products.models import Product
from core.promotions.models import Promotion, ProductPromotion


def apply_rate(amount: float, rate: float, positive=True):
    """ Apply rate to amount"""
    if positive:
        return amount * (1 + rate)
    return amount * (1 - rate)


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

    def get_price(self, items: List['OrderItem'] = None) -> Dict:
        """ Return dict of price per item

        Vat amount, discount amount and total
        """
        result = defaultdict()
        for item in (items or self.items.all()):
            excl_taxes = item.quantity * item.product.price
            incl_taxes = apply_rate(
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

    def get_promotion(self):
        """ Get promotion """
        return self.product.promotions.filter(start_at=self.order.created_at)


class OrderItem2(models.Model):
    """ Order Item to benchmark report metric and response to the test.

    Because the same product could have its price changed over order...

    """
    created_at = models.DateField(default=datetime.now().strftime("%Y-%m-%d"))
    order_id = models.CharField(max_length=50)
    product_id = models.CharField(max_length=50)
    vendor_id = models.CharField(max_length=50)
    product_description = models.CharField(max_length=50)
    product_price = models.FloatField()
    product_vat_rate = models.FloatField()
    discount_rate = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.product_description}/{self.quantity}"

    def get_promotions(self):
        """ Get promotion """
        return Product.objects.get(id=self.product_id).promotions.all()

    def get_commission(self) -> Commission:
        """ Get commission for the vendor related to the date """
        return Commission.objects.filter(
            vendor_id=self.vendor_id, created_at=self.created_at).first()

    def get_price(self) -> Dict:
        """ Return dict of price """
        excl_taxes = self.quantity * self.product_price
        incl_taxes = apply_rate(
            excl_taxes, self.product_vat_rate)
        discounted_amount = float(self.discount_rate) * float(incl_taxes)

        try:
            commission_rate = self.get_commission().rate
        except Exception as error:  # noqa
            commission_rate = 0

        total_amount = incl_taxes - discounted_amount
        commission_amount = float(commission_rate) * float(total_amount)

        return {
            "promotions": [p.promotion.id for p in self.get_promotions()],
            "description": self.product_description,
            "full_price_amount": incl_taxes,
            "discounted_amount": discounted_amount,
            "vat_amount": excl_taxes * self.product_vat_rate,
            "product_vat_rate": self.product_vat_rate,
            "total_amount": total_amount,
            "commission_rate": commission_rate,
            "commission_amount": commission_amount
        }
