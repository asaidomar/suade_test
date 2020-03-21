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
    items = serializers.ReadOnlyField(source="items_count")
    consumers = serializers.ReadOnlyField(source="consumer_count")
    total_discount_amount = serializers.ReadOnlyField(
        source="discounts_amount_sum")
    discount_rate_avg = serializers.ReadOnlyField(source="avg_discount_rate")
    order_total_avg = serializers.ReadOnlyField(source="avg_order_total")

    commissions = serializers.ReadOnlyField()

    class Meta:
        """Meta class information """
        model = Report
        fields = (
            "create_at",
            "items",
            "consumers",
            "total_discount_amount",
            "discount_rate_avg",
            "order_total_avg",
            "commissions"
        )


class ReportSerializer2(serializers.ModelSerializer):
    """ Report serializer  """
    items = serializers.ReadOnlyField(source="items_count2")
    consumers = serializers.ReadOnlyField(source="consumer_count")
    total_discount_amount = serializers.ReadOnlyField(
        source="discounts_amount_sum2")
    discount_rate_avg = serializers.ReadOnlyField(source="avg_discount_rate")
    order_total_avg = serializers.ReadOnlyField(source="avg_order_total2")

    commissions = serializers.ReadOnlyField(source="commissions2")

    class Meta:
        """Meta class information """
        model = Report
        fields = (
            "create_at",
            "items",
            "consumers",
            "total_discount_amount",
            "discount_rate_avg",
            "order_total_avg",
            "commissions"
        )