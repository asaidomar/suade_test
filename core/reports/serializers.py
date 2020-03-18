#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : serializers
# date : 2020-03-18
# project: suade_test
# author : alisaidomar
from rest_framework import serializers

from core.reports.models import Report


class ReportSerializer(serializers.ModelSerializer):
    """ Report serializer  """

    class Meta:
        """Meta class information """
        model = Report
        fields = '__all__'
        read_only_fields = '__all__'
