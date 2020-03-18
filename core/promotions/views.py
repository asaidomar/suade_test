#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : views
# date : 2020-03-16
# project: suade_test
# author : alisaidomar

from rest_framework import viewsets
from rest_framework import permissions

from core.promotions import serializers as promotion_serializers
from core.promotions import models as promotion_models


class DiscountViewSet(viewsets.ModelViewSet):
    """ Discount view Set """
    model = promotion_models.Discount
    serializer_class = promotion_serializers.DiscountSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = promotion_models.Discount.objects


class PromotionViewSet(viewsets.ModelViewSet):
    """ Promotion view Set """
    model = promotion_models.Promotion
    serializer_class = promotion_serializers.PromotionSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = promotion_models.Promotion.objects
