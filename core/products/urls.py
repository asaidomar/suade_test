#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : urls
# date : 2020-03-17
# project: suade_test
# author : alisaidomar
from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from core.products import views

router = DefaultRouter()

router.register(r'products', views.ProductViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
