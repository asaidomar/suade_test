#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : models
# date : 2020-03-17
# project: suade_test
# author : alisaidomar
import datetime

from django.db import models


class Discount(models.Model):
    """ Discount model """
    start_at = models.DateField()
    n_days = models.PositiveIntegerField(default=0)
    rate = models.FloatField()  # 0.5222030877456142

    @property
    def end_date(self) -> datetime.date:
        """ End date """
        return self.start_at + datetime.timedelta(days=self.n_days)

    def __str__(self):
        return str(self.rate)


class Promotion(models.Model):
    """ Promotion model """
    n_days = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=50)
    start_at = models.DateField()

    @property
    def end_date(self) -> datetime.date:
        """ End date """
        return self.start_at + datetime.timedelta(days=self.n_days)

    def __str__(self):
        return str(self.name)


class ProductPromotion(models.Model):
    """ Product promotion """
    start_at = models.DateField()
    product = models.ForeignKey(
        "products.Product",
        on_delete=models.CASCADE,
        related_name="promotions")
    promotion = models.ForeignKey('Promotion', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.promotion}/{self.product}"
