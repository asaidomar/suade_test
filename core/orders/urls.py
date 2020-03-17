#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : urls
# date : 2020-03-17
# project: suade_test
# author : alisaidomar
from django.urls import path

from core.orders import views


urlpatterns = [
    path('members/<int:member_id>/orders', views.OrderListView.as_view(),
         name='order-list'),
    path('orders/<int:pk>', views.OrderView.as_view(),
         name='order-detail'),

    path('orders/<int:order_id>/items', views.OrderItemListView.as_view(),
         name='item-list'),
    path('items/<int:pk>', views.OrderItemView.as_view(),
         name='item-detail'),
]
