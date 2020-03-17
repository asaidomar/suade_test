#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : serializers
# date : 2020-03-17
# project: suade_test
# author : alisaidomar

from rest_framework import serializers
from core.orders import models as order_models


class OrderSerializer(serializers.ModelSerializer):
    """ core.orders.models.Order serializer  """

    class Meta:
        """Meta class information """
        model = order_models.Order
        fields = '__all__'
        read_only_fields = ("pk", "create_at")


class OrderItemSerializer(serializers.ModelSerializer):
    """ core.orders.models.OrderItem serializer  """

    class Meta:
        """Meta class information """
        model = order_models.OrderItem
        fields = '__all__'
        read_only_fields = ("pk", "creation_date", "update_date")
