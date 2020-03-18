#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : urls
# date : 2020-03-18
# project: suade_test
# author : alisaidomar
from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from core.invoices import views

router = DefaultRouter()

router.register(r'commission', views.CommissionViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
