#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : test_invoices
# date : 2020-03-17
# project: suade_test
# author : alisaidomar

import pytest
from django.urls import reverse

from core.invoices import models as invoice_models
from ..base import TestBase


@pytest.mark.urls('config.urls')
@pytest.mark.django_db
class TestCommissionAPI(TestBase):
    """ core.invoices.models.Commission API tests """

    def test_create_commission(self, create_vendor):
        def commission_factory(**kwargs):  # noqa
            return {
                "vendor": create_vendor.pk,
                "rate": 0
            }

        self._test_create_resource(
            reverse("commission-list"),
            invoice_models.Commission,
            commission_factory
        )

    def test_get_commissions(self, create_commission):
        ret = self._test_get_resource(reverse("commission-list"))
        assert create_commission.pk in [m['id'] for m in ret.json()]

    def test_get_commission(self, create_commission):
        path = reverse("commission-detail",
                       kwargs={"pk": create_commission.pk})
        ret = self._test_get_resource(path)
        assert ret.json()['id'] == create_commission.pk

    def test_patch_commission(self, create_commission):
        def commission_factory(**kwargs):  # noqa
            return {
                "rate": create_commission.rate + 10
            }

        path = reverse("commission-detail",
                       kwargs={"pk": create_commission.pk})
        self._test_patch_resource(
            path,
            invoice_models.Commission,
            commission_factory
        )

    def test_delete_commission(self, create_commission):
        path = reverse("commission-detail",
                       kwargs={"pk": create_commission.pk})
        self._test_delete_resource(path)
