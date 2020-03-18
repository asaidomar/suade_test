#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : urls
# date : 2020-03-17
# project: suade_test
# author : alisaidomar

from django.urls import path
from core.reports import views

urlpatterns = [
    path('reports', views.ReportView.as_view(),
         name='report'),
]
