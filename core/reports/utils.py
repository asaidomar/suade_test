#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : utils
# date : 2020-03-18
# project: suade_test
# author : alisaidomar
from core.reports.models import Report


def build_report(orders, created_at):
    """ Create report obj """
    report = Report(create_at=created_at)
    report.save()
    for o in orders:
        report.orders.add(o)
    report.save()
    return report
