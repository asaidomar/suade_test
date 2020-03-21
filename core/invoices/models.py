#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : models
# date : 2020-03-18
# project: suade_test
# author : alisaidomar
from datetime import datetime

from django.db import models


class Commission(models.Model):
    """ Commission model """
    rate = models.FloatField()
    created_at = models.DateField(default=datetime.now().strftime("%Y-%m-%d"))
    vendor = models.ForeignKey("vendors.Vendor",
                               on_delete=models.DO_NOTHING,
                               related_name='commissions')

    def __str__(self):
        return f"{self.vendor}/{self.rate}"
