#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : test_orders
# date : 2020-03-17
# project: suade_test
# author : alisaidomar
from datetime import datetime

import pytest
from django.urls import reverse
from mixer.backend.django import mixer

from core.orders import models as order_models
from core.promotions.models import ProductPromotion
from ..base import TestBase


@pytest.mark.urls('config.urls')
@pytest.mark.django_db
class TestOrderAPI(TestBase):
    """ core.orders.models.Order API tests """

    def test_create_order(self, create_member, create_vendor):
        def order_factory(**kwargs):  # noqa
            return {
                "customer": create_member.pk,
                "vendor": create_vendor.pk,
                "created_at": datetime.now().isoformat(sep=" ")
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

    @staticmethod
    def get_full_price(products_quantity, products_price,
                       products_discount_rate, products_vat_rate):
        price_amount = map(
            lambda args: args[0] * args[1],
            zip(products_price, products_quantity)
        )

        full_price_amount = list(map(
            lambda args: args[0] * (1 + args[1]),
            zip(price_amount, products_vat_rate)
        ))
        discounted_amount = list(map(
            lambda args: args[0] * args[1],
            zip(full_price_amount, products_discount_rate)
        ))
        total_price = sum(full_price_amount) - sum(discounted_amount)
        return total_price

    def test_get_price(self, create_order, create_promotion):
        nb_items = 10
        discount_rate = 0.10
        create_order.vendor.vat_rate = 0.20
        product_price = 10
        quantity = 3
        vat_rate = 0.20
        for i in range(1, nb_items + 1):
            product = mixer.blend(
                    'products.Product',
                    price=i * product_price,
                    code=f"Product_{i}",
                    description=f"Product {i}",
                    vat_rate=vat_rate,
                    vendor=mixer.blend('vendors.Vendor', vat_rate=vat_rate)
                )
            mixer.blend(ProductPromotion,
                        promotion=create_promotion,
                        product=product)
            mixer.blend(
                order_models.OrderItem,
                order=create_order,
                product=product,
                discount=mixer.blend(
                    'promotions.Discount', rate=discount_rate + i),
                quantity=quantity + i
            )

        price = create_order.items_price
        tab = range(1, nb_items + 1)
        expected_total_amount = self.get_full_price(
            products_quantity=[i + quantity for i in tab],
            products_price=[i * product_price for i in tab],
            products_vat_rate=[vat_rate] * nb_items,
            products_discount_rate=[discount_rate + i for i in tab]
        )
        result_tot = int(price["total_amount"]["total_amount"])
        assert result_tot == int(expected_total_amount)
