#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : views
# date : 2020-03-17
# project: suade_test
# author : alisaidomar
from rest_framework import permissions

from rest_framework import generics
from core.orders import serializers as order_serializers
from core.orders import models as order_models


class OrderListView(generics.ListCreateAPIView):
    """ Order view """
    serializer_class = order_serializers.OrderSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = order_models.Order.objects
    lookup_url_kwarg = "member_id"

    def get_queryset(self):
        customer_id = self.kwargs.get(self.lookup_url_kwarg)
        orders = order_models.Order.objects.filter(customer=customer_id)
        return orders


class OrderView(generics.RetrieveUpdateDestroyAPIView):
    """ RUD on order resource """
    serializer_class = order_serializers.OrderSerializer
    lookup_url_kwarg = 'pk'
    queryset = order_models.Order.objects.filter()


class OrderItemListView(generics.ListCreateAPIView):
    """ Order view """
    serializer_class = order_serializers.OrderItemSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = order_models.OrderItem.objects
    lookup_url_kwarg = "order_id"

    def get_queryset(self):
        order_id = self.kwargs.get(self.lookup_url_kwarg)
        orders = order_models.OrderItem.objects.filter(order=order_id)
        return orders


class OrderItemView(generics.RetrieveUpdateDestroyAPIView):
    """ RUD on item resource """
    serializer_class = order_serializers.OrderItemSerializer
    lookup_url_kwarg = 'pk'
    queryset = order_models.OrderItem.objects.filter()
