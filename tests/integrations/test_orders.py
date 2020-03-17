#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : test_orders
# date : 2020-03-17
# project: suade_test
# author : alisaidomar

import pytest
from django.urls import reverse

from core.orders import models as order_models
from ..base import TestBase


@pytest.mark.urls('config.urls')
@pytest.mark.django_db
class TestOrderAPI(TestBase):
    """ core.orders.models.Order API tests """

    def test_create_order(self, create_member, create_vendor):
        def order_factory(**kwargs):  # noqa
            return {
                "customer": create_member.pk,
                "vendor": create_vendor.pk
            }

        self._test_create_resource(
            reverse("order-list", kwargs={'member_id': create_member.id}),
            order_models.Order,
            order_factory
        )

    def test_get_orders(self, create_order):
        path = reverse(
            "order-list", kwargs={"member_id": create_order.customer.id})
        ret = self._test_get_resource(path)
        assert create_order.pk in [m['id'] for m in ret.json()]

    def test_get_order(self, create_order):
        path = reverse("order-detail",
                       kwargs={"pk": create_order.pk})
        ret = self._test_get_resource(path)
        assert ret.json()['id'] == create_order.pk

    def test_delete_order(self, create_order):
        path = reverse("order-detail",
                       kwargs={"pk": create_order.pk})
        self._test_delete_resource(path)


@pytest.mark.urls('config.urls')
@pytest.mark.django_db
class TestOrderItemAPI(TestBase):
    """ core.orders.models.OrderItem API tests """

    def test_create_item(self, create_order, create_product, create_discount):
        def item_factory(**kwargs):  # noqa
            return {
                "quantity": 1,
                "order": create_order.pk,
                "product": create_product.pk,
                "discount": create_discount.pk
            }
        path = reverse("item-list", kwargs={"order_id": create_order.pk})
        self._test_create_resource(
            path,
            order_models.OrderItem,
            item_factory
        )

    def test_get_items(self, create_item):
        path = reverse("item-list", kwargs={"order_id": create_item.order.pk})
        ret = self._test_get_resource(path)
        assert create_item.pk in [m['id'] for m in ret.json()]

    def test_get_item(self, create_item):
        path = reverse("item-detail",
                       kwargs={"pk": create_item.pk})
        ret = self._test_get_resource(path)
        assert ret.json()['id'] == create_item.pk

    def test_delete_item(self, create_item):
        path = reverse("item-detail",
                       kwargs={"pk": create_item.pk})
        self._test_delete_resource(path)
