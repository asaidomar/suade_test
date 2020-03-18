#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : serializers
# date : 2020-03-18
# project: suade_test
# author : alisaidomar
from rest_framework import serializers

from core.reports.models import Report


class ReportSerializer(serializers.ModelSerializer):
    """ Report serializer  """
    items_count = serializers.ReadOnlyField()
    consumer_count = serializers.ReadOnlyField()
    discounts_amount_sum = serializers.ReadOnlyField()
    avg_discount_rate = serializers.ReadOnlyField()
    avg_order_total = serializers.ReadOnlyField()

    commissions = serializers.ReadOnlyField()

    class Meta:
        """Meta class information """
        model = Report
        fields = (
            "create_at",
            "items_count",
            "consumer_count",
            "discounts_amount_sum",
            "avg_discount_rate",
            "avg_order_total",
            "commissions",
        )
