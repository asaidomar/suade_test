#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : urls
# date : 2020-03-16
# project: suade_test
# author : alisaidomar
from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from core.members import views

router = DefaultRouter()

router.register(r'members', views.MemberViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
