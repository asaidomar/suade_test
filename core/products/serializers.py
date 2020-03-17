#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : serializers
# date : 2020-03-17
# project: suade_test
# author : alisaidomar

from rest_framework import serializers
from core.products import models as product_models


class ProductSerializer(serializers.ModelSerializer):
    """ core.products.models.Product serializer  """

    class Meta:
        """Meta class information """
        model = product_models.Product
        fields = '__all__'
        read_only_fields = ("pk", "creation_date", "update_date")
