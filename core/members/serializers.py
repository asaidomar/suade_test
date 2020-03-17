#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : serializers
# date : 2020-03-17
# project: suade_test
# author : alisaidomar

from rest_framework import serializers
from core.members import models as member_models


class MemberSerializer(serializers.ModelSerializer):
    """ core.members.models.Member serializer """
    class Meta:
        """Meta class information """
        model = member_models.Member
        fields = '__all__'
        read_only_fields = ("pk", )
