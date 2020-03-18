#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : utils
# date : 2020-03-18
# project: suade_test
# author : alisaidomar
from core.reports.models import Report


def build_report(orders, created_at):
    report = Report(create_at=created_at)
    report.save()
    report.orders.set(orders)
    return report
