#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : test_products
# date : 2020-03-17
# project: suade_test
# author : alisaidomar

import pytest
from django.urls import reverse
from mixer.backend.django import mixer

from core.products import models as product_models
from ..base import TestBase


@pytest.mark.urls('config.urls')
@pytest.mark.django_db
class TestProductAPI(TestBase):
    """ core.products.models.VendorProduct API tests """

    def test_create_product(self, create_vendor):
        def product_factory(**kwargs):  # noqa
            return {
                "code": str(id(mixer.FAKE)),
                "brand": "string",
                "description": "string",
                "price": 10,
                "currency": "Euros",
                "vendor": create_vendor.pk
            }

        self._test_create_resource(
            reverse("product-list"),
            product_models.Product,
            product_factory
        )

    def test_get_products(self, create_product):
        ret = self._test_get_resource(reverse("product-list"))
        assert create_product.pk in [m['id'] for m in ret.json()]

    def test_get_product(self, create_product):
        path = reverse("product-detail",
                       kwargs={"pk": create_product.pk})
        ret = self._test_get_resource(path)
        assert ret.json()['id'] == create_product.pk

    def test_patch_product(self, create_product):
        def product_factory(**kwargs):  # noqa
            return {
                "description": create_product.description + " Update"
            }

        path = reverse("product-detail",
                       kwargs={"pk": create_product.pk})
        self._test_patch_resource(
            path,
            product_models.Product,
            product_factory
        )

    def test_delete_product(self, create_product):
        path = reverse("product-detail",
                       kwargs={"pk": create_product.pk})
        self._test_delete_resource(path)
