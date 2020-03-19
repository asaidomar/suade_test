#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : urls
# date : 2020-03-17
# project: suade_test
# author : alisaidomar
from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from core.promotions import views

router = DefaultRouter()

router.register(r'discounts', views.DiscountViewSet)
router.register(r'promotions', views.PromotionViewSet)
router.register(r'products_promotion', views.ProductPromotionViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
