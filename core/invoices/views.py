#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : views
# date : 2020-03-16
# project: suade_test
# author : alisaidomar

from rest_framework import viewsets
from rest_framework import permissions

from core.invoices import serializers as invoice_serializers
from core.invoices import models as invoice_models


class CommissionViewSet(viewsets.ModelViewSet):
    """ Promotion view Set """
    model = invoice_models.Commission
    serializer_class = invoice_serializers.CommissionSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = invoice_models.Commission.objects
