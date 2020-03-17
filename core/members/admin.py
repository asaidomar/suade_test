#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : admin
# date : 2020-03-16
# project: suade_test
# author : alisaidomar

from django.contrib import admin
from core.members import models as member_models


@admin.register(member_models.Member)
class MemberAdmin(admin.ModelAdmin):
    """ Member Admin """
    pass
