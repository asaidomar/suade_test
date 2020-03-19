#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : load_data
# date : 2020-03-19
# project: suade_test
# author : alisaidomar
import csv
import pathlib
from datetime import datetime

from mixer.backend.django import mixer
from django.conf import settings
from django.core.management.base import BaseCommand


from core.members import models as member_models
from core.vendors import models as vendor_models
from core.products import models as product_models
from core.orders import models as order_models
from core.promotions import models as promotion_models
from core.invoices import models as invoice_models

data_folder = pathlib.Path(settings.BASE_DIR).joinpath("fixtures", "data")


def create_vendors_orders_cutomers():
    try:
        vendor_file = data_folder.joinpath("orders.csv")

        with vendor_file.open() as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    mixer.blend(
                        member_models.Member, id=row["customer_id"])
                except:
                    pass
                try:
                    mixer.blend(
                        vendor_models.Vendor, id=row["vendor_id"], vat_rate=20)
                except:
                    pass
                mixer.blend(
                    order_models.Order, created_at=row["created_at"])
    except Exception as error:
        pass


def create_products():
    vendor_file = data_folder.joinpath("products.csv")
    with vendor_file.open() as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            mixer.blend(
                product_models.Product,
                id=row["id"],
                description=row['description'],
                brand=row['description'].split()[0],
                currency="Euros"
            )


def create_orders_items():
    vendor_file = data_folder.joinpath("order_lines.csv")

    with vendor_file.open() as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            discount_rate = int(float(row["discount_rate"]) * 100)
            discount, created = promotion_models.Discount.objects.get_or_create(
                rate=discount_rate, n_days=100,
                start_at=datetime.now().strftime("%Y-%m-%d"))
            try:
                product = product_models.Product.objects.get(id=row["product_id"])
            except:
                continue

            product.vendor.vat_rate = int(float(row["product_vat_rate"]) * 100)
            product.vendor.save()
            product.price = row["product_price"]
            product.save()
            try:
                order = order_models.Order.objects.get(id=row["order_id"])
            except:
                continue
            mixer.blend(
                order_models.OrderItem,
                order=order,
                product=product,
                quantity=row["quantity"],
                discount=discount
            )


def create_products_promotions():
    promotions = data_folder.joinpath("product_promotions.csv")

    with promotions.open() as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            product = product_models.Product.objects.get(
                id=row["product_id"])
            promotion = promotion_models.Promotion.objects.get(
                id=row["promotion_id"])
            try:
                mixer.blend(
                    promotion_models.ProductPromotion,
                    promotion=promotion,
                    product=product,
                )
            except:
                continue


def create_promotions():
    promotions = data_folder.joinpath("promotions.csv")

    with promotions.open() as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            mixer.blend(
                promotion_models.Promotion,
                id=row["id"],
                name=row["description"],
                start_at=datetime.now().strftime("%Y-%m-%d"),
            )

def create_commission():
    promotions = data_folder.joinpath("commissions.csv")
    with promotions.open() as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            vendor = vendor_models.Vendor.objects.get(id=row["vendor_id"])
            rate = int(float(row["rate"]) * 100)
            try:
                com, created = invoice_models.Commission.objects.get_or_create(
                    rate=rate,  vendor=vendor)
                com.rate = rate
                com.save()
            except:
                continue


class Command(BaseCommand):
    help = 'Load data'

    def handle(self, *args, **options):
        create_vendors_orders_cutomers()
        create_products()
        create_orders_items()
        create_promotions()
        create_products_promotions()
        create_commission()
