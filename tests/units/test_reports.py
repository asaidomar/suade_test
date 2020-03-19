#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : test_reports
# date : 2020-03-18
# project: suade_test
# author : alisaidomar
import random
from datetime import datetime

import pytest
from mixer.backend.django import mixer

from core.invoices.models import Commission
from core.orders.models import Order, OrderItem
from core.products.models import Product
from core.promotions.models import Discount, Promotion
from core.reports.utils import build_report


@pytest.fixture
def create_report(create_order, create_vendor):
    mixer.blend(Commission, rate=10, vendor=create_vendor)
    nb_orders = 10
    orders = mixer.cycle(nb_orders).blend(Order, vendor=create_vendor)
    for order in orders:
        product = mixer.blend(Product)
        mixer.blend(Promotion, rate=10, product=product)
        mixer.cycle(nb_orders).blend(
            OrderItem,
            order=order,
            quantity=random.randint(1, 100),
            discount=mixer.blend(Discount, rate=20),
            product=product,
        )
    report = build_report(
        orders, created_at=datetime.now().strftime("%Y-%m-%d"))
    assert len(report.orders.all()) == nb_orders
    return report


@pytest.mark.django_db
def test_report_items(create_report):
    expected = [
        sum([i.quantity for i in o.items.all()])
        for o in create_report.orders.all()
    ]
    assert create_report.items_count == sum(expected)


@pytest.mark.django_db
def test_report_consumers(create_report):
    expected = [
        o.customer.id
        for o in create_report.orders.all()
    ]

    computed = create_report.consumers
    assert len(computed) == len(expected)
    assert create_report.consumer_count == len(expected)


@pytest.mark.django_db
def test_report_discount_amount(create_report):
    expected_sum = sum(
        [
            o.items_price["total_amount"]["discounted_amount"]
            for o in create_report.orders.all()
        ]
    )

    computed_sum = sum(create_report.discounts_amount)
    assert computed_sum == expected_sum


@pytest.mark.django_db
def test_report_avg_discount(create_report):
    rates = []
    for o in create_report.orders.all():
        for i in o.items.all():
            rates.extend([i.discount.rate] * i.quantity)

    computes_avg = sum(rates) / len(rates)
    assert computes_avg == create_report.avg_discount_rate


@pytest.mark.django_db
def test_report_avg_total(create_report):
    expected_sum = sum(
        [
            o.items_price["total_amount"]["total_amount"]
            for o in create_report.orders.all()
        ]
    )
    expected = expected_sum / create_report.orders.count()
    assert create_report.avg_order_total == expected


@pytest.mark.django_db
def test_commissions_amount(create_report):
    expected_sum = sum(
        [
            o.items_price["total_amount"]["total_amount"] *
            (o.vendor.commission.rate / 100)
            for o in create_report.orders.all()
        ]
    )
    commission = create_report.commissions_amount
    assert int(commission) == int(expected_sum)


@pytest.mark.django_db
def test_commission_per_promotion(create_report):
    commission_per_promotion = create_report.commissions_promotions
    product_set = set()
    for order in create_report.orders.all():
        for item in order.items.all():
            product_set.add(item.product.promotion.id)
    assert set(commission_per_promotion.keys()) == product_set