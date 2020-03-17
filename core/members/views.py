#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : views
# date : 2020-03-16
# project: suade_test
# author : alisaidomar

from rest_framework import viewsets
from rest_framework import permissions

from core.members import serializers as member_serializers
from core.members import models as member_models


class MemberViewSet(viewsets.ModelViewSet):
    """ Member view Set """
    model = member_models.Member
    serializer_class = member_serializers.MemberSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = member_models.Member.objects
