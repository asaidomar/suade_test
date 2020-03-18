#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : serializers
# date : 2020-03-18
# project: suade_test
# author : alisaidomar

from rest_framework import serializers
from core.invoices import models as invoice_models


class CommissionSerializer(serializers.ModelSerializer):
    """ core.invoices.models.Commission serializer """
    end_date = serializers.ReadOnlyField()

    class Meta:
        """Meta class information """
        model = invoice_models.Commission
        fields = '__all__'
        read_only_fields = ("pk", "created_at")
