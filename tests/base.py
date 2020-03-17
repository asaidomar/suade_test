#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : base
# date : 2020-03-17
# project: suade_test
# author : alisaidomar
import pytest
from django.contrib.auth.models import User

from mixer.backend.django import mixer

from rest_framework.test import APIClient
from core.members import models as member_models


@pytest.mark.urls('config.urls')
@pytest.mark.django_db
class TestBase:
    """ Base class of all integration tests,
    provides an authenticated api client"""

    def setup_method(self):
        self.api_client = APIClient()
        self.user = mixer.blend(User)
        self.api_client = APIClient()
        self.api_client.force_authenticate(self.user)

    def _test_create_resource(self, path, model, *factories, **kwargs):
        data = {}
        for factory in factories:
            data.update(factory(**kwargs))
        ret = self.api_client.post(path=path, data=data, format="json")
        assert ret.status_code == 201
        assert model.objects.first().pk == ret.json()["id"]
        return ret

    def _test_get_resource(self, path):
        ret = self.api_client.get(path=path, format="json")
        assert ret.status_code == 200
        return ret

    def _test_patch_resource(self, path, model, *factories, **kwargs):
        data = {}
        for factory in factories:
            data.update(factory(**kwargs))
        ret = self.api_client.patch(path=path, data=data, format="json")
        assert ret.status_code == 200
        assert model.objects.first().pk == ret.json()["id"]
        return ret

    def _test_delete_resource(self, path):
        ret = self.api_client.delete(path=path, format="json")
        assert ret.status_code == 204
        return ret
