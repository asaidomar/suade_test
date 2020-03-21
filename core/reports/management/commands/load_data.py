#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : load_data
# date : 2020-03-19
# project: suade_test
# author : alisaidomar
# noqa
import csv
import pathlib
from datetime import datetime

from mixer.backend.django import mixer, faker
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
    print("Generate vendors and customers")
    try:
        vendor_file = data_folder.joinpath("orders.csv")

        with vendor_file.open() as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    customer = member_models.Member.objects.filter(
                        id=row["customer_id"]).first()
                    if not customer:
                        customer = mixer.blend(
                            member_models.Member,
                            id=row["customer_id"],
                            tel=faker.phone_number()
                        )
                        print(f"Member {customer} generated.")
                except:  # noqa
                    pass
                try:
                    vendor = vendor_models.Vendor.objects.filter(
                        id=row["vendor_id"]).first()
                    if not vendor:
                        vendor = mixer.blend(
                            vendor_models.Vendor,
                            id=row["vendor_id"],
                            vat_rate=20,
                            name=faker.company())
                        print(f"Vendor {vendor} generated.")
                except:  # noqa
                    pass
                order, created = order_models.Order.objects.get_or_create(
                    id=row["id"],
                    created_at=row["created_at"],
                    vendor=vendor,
                    customer=customer)
                print(f"Order {order} generated.")
    except Exception:
        pass


def create_products():
    print("Generate products...")
    vendor_file = data_folder.joinpath("products.csv")
    with vendor_file.open() as csvfile:
        reader = csv.DictReader(csvfile)
        vendor = vendor_models.Vendor.objects.first()
        for row in reader:
            p = mixer.blend(
                product_models.Product,
                id=row["id"],
                description=row['description'],
                brand=row['description'].split()[0],
                currency="Euros",
                vendor=vendor
            )
            print(f"Product {p} generated.")


def create_orders_items2():
    print("Generate Order items...")
    vendor_file = data_folder.joinpath("order_lines.csv")

    with vendor_file.open() as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            product = product_models.Product.objects.get(id=row["product_id"])
            order = order_models.Order.objects.get(id=row["order_id"])
            product.vendor = order.vendor
            product.save()

            item, created = order_models.OrderItem2.objects.get_or_create(
                order_id=row["order_id"],
                product_id=row["product_id"],
                product_description=row["product_description"],
                product_price=row["product_price"],
                discount_rate=row["discount_rate"],
                quantity=row["quantity"],
                product_vat_rate=row["product_vat_rate"],
                vendor_id=order.vendor_id,
                created_at=order.created_at
            )
            print(f"Order Item {item} generated.")


def create_orders_items():
    print("Generate Order items...")
    vendor_file = data_folder.joinpath("order_lines.csv")

    with vendor_file.open() as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            discount_rate = float(row["discount_rate"])
            discount, created = promotion_models.Discount.objects.get_or_create(
                rate=discount_rate, n_days=100,
                start_at="1900-01-01")
            try:
                product = product_models.Product.objects.get(
                    id=row["product_id"])
                product.vendor.vat_rate = float(row["product_vat_rate"])
                product.vendor.save()
                product.price = row["product_price"]
                product.vat_rate = float(row["product_vat_rate"])
                product.save()
            except:  # noqa
                continue
            try:
                order = order_models.Order.objects.get(id=row["order_id"])
                product.vendor = order.vendor
                product.save()
            except:  # noqa
                continue

            try:
                item, created = order_models.OrderItem.objects.get_or_create(
                    order=order,
                    product=product,
                    quantity=row["quantity"],
                    discount=discount
                )
                print(f"Order Intem {item} generated.")
            except:  # noqa
                pass


def create_products_promotions():
    print("Generate products promotions")
    promotions = data_folder.joinpath("product_promotions.csv")

    with promotions.open() as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            product = product_models.Product.objects.get(
                id=row["product_id"])
            promotion = promotion_models.Promotion.objects.get(
                id=row["promotion_id"])
            try:
                pp, created = \
                    promotion_models.ProductPromotion.objects.get_or_create(  # noqa
                    start_at=row["date"],
                    promotion=promotion,
                    product=product,
                )
                print(f"Product Promotion {pp} generated.")
            except:  # noqa
                continue


def create_promotions():
    print("Generate Promotion")
    promotions = data_folder.joinpath("promotions.csv")

    with promotions.open() as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            p = mixer.blend(
                promotion_models.Promotion,
                id=row["id"],
                name=row["description"],
                start_at=datetime.now().strftime("%Y-%m-%d"),
            )
            print(f"Promotion {p} generated.")


def create_commission():
    print("Generate Commission")
    promotions = data_folder.joinpath("commissions.csv")
    with promotions.open() as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            vendor = vendor_models.Vendor.objects.get(id=row["vendor_id"])
            rate = float(row["rate"])
            try:
                com, created = invoice_models.Commission.objects.get_or_create(
                    rate=rate, vendor=vendor, created_at=row["date"])
                print(f"Commission {com} generated.")
            except:  # noqa
                continue


class Command(BaseCommand):
    help = 'Load data'

    def handle(self, *args, **options):
        create_vendors_orders_cutomers()
        create_products()
        create_orders_items()
        create_orders_items2()
        create_promotions()
        create_products_promotions()
        create_commission()
