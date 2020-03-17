#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : views
# date : 2020-03-17
# project: suade_test
# author : alisaidomar

from rest_framework import viewsets
from rest_framework import permissions

from core.products import serializers as product_serializers
from core.products import models as product_models


class ProductViewSet(viewsets.ModelViewSet):
    """ Product view Set """
    model = product_models.Product
    serializer_class = product_serializers.ProductSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = product_models.Product.objects
