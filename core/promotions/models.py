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
    amount = models.PositiveIntegerField()   # percent 50 => 50%

    @property
    def end_date(self) -> datetime.date:
        """ End date """
        return self.start_at + datetime.timedelta(days=self.n_days)
