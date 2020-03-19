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
from core.products import models as product_models
from core.orders import models as order_models
from core.promotions import models as promotion_models
from core.invoices import models as invoice_models


@pytest.fixture(autouse=True, scope="session")
def setup_env():
    """ Set test environment variables """
    os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings.test"


@pytest.fixture
def create_member() -> member_models.Member:
    """ core.vendors.models.VendorTag fixture  """
    member_obj = mixer.blend(member_models.Member)
    return member_obj


@pytest.fixture
def create_user() -> member_models.User:
    """ django.contrib.auth.models.User fixture  """
    member_obj = mixer.blend(member_models.User)
    return member_obj


@pytest.fixture
def api_client(create_member) -> APIClient:
    """ Return an authenticated api client """
    api_client = APIClient()
    api_client.force_authenticate(create_member)
    return api_client


@pytest.fixture
def create_tag() -> vendor_models.VendorTag:
    """ core.vendors.models.VendorTag fixture  """
    tag_obj = mixer.blend(vendor_models.VendorTag)
    return tag_obj


@pytest.fixture
def create_category() -> vendor_models.VendorCategory:
    """ core.vendors.models.VendorCategory fixture  """
    category_obj = mixer.blend(vendor_models.VendorCategory)
    return category_obj


@pytest.fixture
def create_review() -> vendor_models.VendorReview:
    """ core.vendors.models.VendorReview fixture  """
    review_obj = mixer.blend(vendor_models.VendorReview)
    return review_obj


@pytest.fixture
def create_vendor() -> vendor_models.Vendor:
    """ core.vendors.models.Vendor fixture  """
    vender_obj = mixer.blend(vendor_models.Vendor)
    return vender_obj


@pytest.fixture
def create_product() -> product_models.Product:
    """ core.products.models.Product fixture  """
    product_obj = mixer.blend(product_models.Product)
    return product_obj


@pytest.fixture
def create_order() -> order_models.Order:
    """ core.orders.models.Order fixture  """
    order_obj = mixer.blend(order_models.Order)
    return order_obj


@pytest.fixture
def create_item() -> order_models.OrderItem:
    """ core.orders.models.OrderItem fixture  """
    item_obj = mixer.blend(order_models.OrderItem)
    return item_obj


@pytest.fixture
def create_discount() -> promotion_models.Discount:
    """ core.promotions.models.Discount fixture  """
    discount_obj = mixer.blend(promotion_models.Discount)
    return discount_obj


@pytest.fixture
def create_commission() -> invoice_models.Commission:
    """ core.invoices.models.Commission fixture  """
    commission_obj = mixer.blend(invoice_models.Commission)
    return commission_obj


@pytest.fixture
def create_promotion() -> promotion_models.Promotion:
    """ core.promotions.models.Promotion fixture  """
    promotion_obj = mixer.blend(promotion_models.Promotion)
    return promotion_obj


@pytest.fixture
def create_product_promotion(create_promotion) -> \
        promotion_models.ProductPromotion:
    """ core.promotions.models.Promotion fixture  """
    promotion_obj = mixer.blend(promotion_models.ProductPromotion,
                                promotion=create_promotion)
    return promotion_obj
