#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : test_members
# date : 2020-03-17
# project: suade_test
# author : alisaidomar
from random import randint

import pytest
from django.urls import reverse

from core.members import models as member_models
from ..base import TestBase


@pytest.mark.urls('config.urls')
@pytest.mark.django_db
class TestMemberAPI(TestBase):
    """ core.members.models.VendorMember API tests """

    def test_create_member(self, create_user):

        def member_factory(**kwargs):  # noqa
            return {
                "tel": "string",
                "civility": "Mrs",
                "birthday": "2020-03-17",
                "city": "string",
                "country": "string",
                "address": "string",
                "user": create_user.pk
            }

        self._test_create_resource(
            reverse("member-list"),
            member_models.Member,
            member_factory
        )

    def test_get_members(self, create_member):
        ret = self._test_get_resource(reverse("member-list"))
        assert create_member.pk in [m['id'] for m in ret.json()]

    def test_get_member(self, create_member):
        path = reverse("member-detail",
                       kwargs={"pk": create_member.pk})
        ret = self._test_get_resource(path)
        assert ret.json()['id'] == create_member.pk

    def test_patch_member(self, create_member):

        def member_factory(**kwargs):  # noqa
            return {
                "city": create_member.city + "Update"
            }

        path = reverse("member-detail",
                       kwargs={"pk": create_member.pk})
        self._test_patch_resource(
            path,
            member_models.Member,
            member_factory
        )

    def test_delete_member(self, create_member):
        path = reverse("member-detail",
                       kwargs={"pk": create_member.pk})
        self._test_delete_resource(path)
