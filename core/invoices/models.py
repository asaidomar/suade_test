#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : models
# date : 2020-03-18
# project: suade_test
# author : alisaidomar

from django.db import models


class Commission(models.Model):
    """ Commission model """
    rate = models.PositiveIntegerField()
    created_at = models.DateField(auto_now_add=True)
    vendor = models.OneToOneField("vendors.Vendor",
                                  on_delete=models.DO_NOTHING,
                                  related_name='commission')
