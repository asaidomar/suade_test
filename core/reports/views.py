#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : views
# date : 2020-03-18
# project: suade_test
# author : alisaidomar
from datetime import datetime

import django.core.exceptions

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, generics
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from core.orders.models import Order
from core.reports import serializers as report_serializers
from core.reports.models import Report
from core.reports.utils import build_report
from logger import get_logger

logger = get_logger(__file__)


class StandardResultsSetPagination(PageNumberPagination):
    """ Pagination class, provides query parameters """
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class ReportView(generics.GenericAPIView):
    """ Report API """
    serializer_class = report_serializers.ReportSerializer
    permission_classes = (permissions.IsAuthenticated,)

    day_param = openapi.Parameter(
        'day', openapi.IN_QUERY,
        description="Day of report (YYYY-MM-DD)",
        type=openapi.FORMAT_DATE,
        default=datetime.now().strftime("%Y-%m-%d"))

    def get_queryset(self):
        day = self.request.query_params.get(
            'day', datetime.now().strftime("%Y-%m-%d"))
        orders = Order.objects.filter(created_at__date=day)
        return orders

    @swagger_auto_schema(
        manual_parameters=[day_param],
        responses={
            200: openapi.Response(
                'Report of day ', report_serializers.ReportSerializer),
        })
    def get(self, request, *args, **kwargs):
        try:
            day = self.request.query_params.get(
                'day', datetime.now().strftime("%Y-%m-%d"))
            logger.info(f"Getting report for {day}...")
            if report := Report.objects.filter(create_at=day).first():  # noqa
                logger.info(f"Report exists from db")
                return Response(self.get_serializer(report).data)
            orders = self.get_queryset()
            logger.info("Generate report from orders...")
            report = build_report(orders, day)
            return Response(self.get_serializer(report).data)
        except (ValidationError,
                django.core.exceptions.ValidationError) as error:
            return Response(data=error, status=400)
