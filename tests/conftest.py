#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : conftest
# date : 2020-03-17
# project: suade_test
# author : alisaidomar
""" Fixtures module  """
import os

import pytest

from rest_framework.test import APIClient
from mixer.backend.django import mixer

from core.members import models as member_models
from core.vendors import models as vendor_models


@pytest.fixture(autouse=True, scope="session")
def setup_env():
    """ Set test environment variables """
    os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings.test"


@pytest.fixture
def create_member():
    """ core.vendors.models.VendorTag fixture  """
    member_obj = mixer.blend(member_models.Member)
    return member_obj


@pytest.fixture
def create_user():
    """ django.contrib.auth.models.User fixture  """
    member_obj = mixer.blend(member_models.User)
    return member_obj


@pytest.fixture
def api_client(create_member):
    """ Return an authenticated api client """
    api_client = APIClient()
    api_client.force_authenticate(create_member)
    return api_client


@pytest.fixture
def create_tag():
    """ core.vendors.models.VendorTag fixture  """
    tag_obj = mixer.blend(vendor_models.VendorTag)
    return tag_obj


@pytest.fixture
def create_category():
    """ core.vendors.models.VendorCategory fixture  """
    category_obj = mixer.blend(vendor_models.VendorCategory)
    return category_obj


@pytest.fixture
def create_review():
    """ core.vendors.models.VendorReview fixture  """
    category_obj = mixer.blend(vendor_models.VendorReview)
    return category_obj


@pytest.fixture
def create_vendor():
    """ core.vendors.models.Vendor fixture  """
    category_obj = mixer.blend(vendor_models.Vendor)
    return category_obj
