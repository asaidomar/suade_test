#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : test_promotions
# date : 2020-03-17
# project: suade_test
# author : alisaidomar
from datetime import datetime

import pytest
from django.urls import reverse

from core.promotions import models as promotion_models
from ..base import TestBase


@pytest.mark.urls('config.urls')
@pytest.mark.django_db
class TestDiscountAPI(TestBase):
    """ core.promotions.models.Discount API tests """

    def test_create_discount(self):
        def discount_factory(**kwargs):  # noqa
            return {
                "start_at": datetime.now().strftime("%Y-%m-%d"),
                "n_days": 0,
                "amount": 0
            }

        self._test_create_resource(
            reverse("discount-list"),
            promotion_models.Discount,
            discount_factory
        )

    def test_get_promotions(self, create_discount):
        ret = self._test_get_resource(reverse("discount-list"))
        assert create_discount.pk in [m['id'] for m in ret.json()]

    def test_get_discount(self, create_discount):
        path = reverse("discount-detail",
                       kwargs={"pk": create_discount.pk})
        ret = self._test_get_resource(path)
        assert ret.json()['id'] == create_discount.pk

    def test_patch_discount(self, create_discount):
        def discount_factory(**kwargs):  # noqa
            return {
                "amout": create_discount.amount + 10
            }

        path = reverse("discount-detail",
                       kwargs={"pk": create_discount.pk})
        self._test_patch_resource(
            path,
            promotion_models.Discount,
            discount_factory
        )

    def test_delete_discount(self, create_discount):
        path = reverse("discount-detail",
                       kwargs={"pk": create_discount.pk})
        self._test_delete_resource(path)
