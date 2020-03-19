#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : serializers
# date : 2020-03-17
# project: suade_test
# author : alisaidomar

from rest_framework import serializers
from core.promotions import models as promotion_models


class DiscountSerializer(serializers.ModelSerializer):
    """ core.promotions.models.Promotion serializer """
    end_date = serializers.ReadOnlyField()

    class Meta:
        """Meta class information """
        model = promotion_models.Discount
        fields = '__all__'
        read_only_fields = ("pk", 'end_date')


class ProductPromotionSerializer(serializers.ModelSerializer):
    """ core.promotions.models.ProductPromotion serializer """

    class Meta:
        """Meta class information """
        model = promotion_models.ProductPromotion
        fields = '__all__'
        read_only_fields = ("pk", 'end_date')


class PromotionSerializer(serializers.ModelSerializer):
    """ core.promotions.models.Promotion serializer """
    end_date = serializers.ReadOnlyField()

    class Meta:
        """Meta class information """
        model = promotion_models.Promotion
        fields = '__all__'
        read_only_fields = ("pk", 'end_date')
