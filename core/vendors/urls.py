#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : urls
# date : 2020-03-16
# project: suade_test
# author : alisaidomar
from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from core.vendors import views

router = DefaultRouter()

router.register(r'vendors', views.VendorViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'reviews', views.ReviewViewSet)
router.register(r'categories', views.CategoryViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
