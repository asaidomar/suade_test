from collections import defaultdict
from typing import List, Dict, Tuple

from django.db import models
from django.utils.functional import cached_property

from logger import get_logger

logger = get_logger(__file__)


class Report(models.Model):
    """ Report model """
    create_at = models.DateField()
    orders = models.ManyToManyField("orders.Order")

    def __str__(self):
        return f"{self.create_at}"

    @property
    def prefetched_query(self):
        return Report.objects.prefetch_related(
            "orders__customer",
            "orders__items__product",
            "orders__items__discount",
            "orders__vendor__commission",
            "orders__items__product__promotion"
        )

    @property
    def items(self):
        """ Items for day self.create_at """
        return self.prefetched_query.filter(
            create_at=self.create_at).values("orders__items__quantity")

    @property
    def items_count(self):
        """ Items count for day self.create_at """
        return sum(i["orders__items__quantity"] or 0 for i in self.items)

    @property
    def consumers(self):
        """ Consumer for the day create_at """
        return self.prefetched_query.filter(
            create_at=self.create_at).values("orders__customer__id")

    @property
    def consumer_count(self):
        """ Consumer Count for the day create_at """
        return self.consumers.count()

    @cached_property  # instance cached
    def items_price(self) -> List[Dict]:
        """ list of core.orders.models.Order.items_price one per order.

        """
        reports = self.prefetched_query.filter(
            create_at=self.create_at)
        return [o.items_price for o in reports.first().orders.all()]

    @property
    def discounts_amount(self):
        """ Discounts amount for the day create_at """
        return [
            i["total_amount"]["discounted_amount"] for i in self.items_price
        ]

    @property
    def discounts_amount_sum(self):
        """ The count """
        return sum(self.discounts_amount)

    @property
    def avg_discount_rate(self):
        """ Item for day self.create_at """
        discounts = self.prefetched_query.filter(
            create_at=self.create_at).values(
            "orders__items__discount__rate", "orders__items__quantity")

        tot = sum(d["orders__items__quantity"] or 0 for d in discounts)
        rates = sum(
            (d["orders__items__quantity"] or 0) *
            (d["orders__items__discount__rate"] or 0)
            for d in discounts
        )
        if tot == 0:
            return 0
        return rates / tot

    @property
    def avg_order_total(self):
        """ The average order total for the day create_at """
        total = sum([
            i["total_amount"]["total_amount"] for i in self.items_price
        ])
        n_order = len(self.items_price)
        if n_order == 0:
            return 0
        return total / n_order

    @cached_property
    def commissions_vendor(self) -> Tuple[Dict, int]:
        """ Per vendor list of commission amount;
        Make a groupby-like against order.vendor.pk
        """
        result = defaultdict(list)
        tot = 0
        for order, amount_dict in self.iter_orders:
            result[order.vendor.pk].append(amount_dict)
            tot += amount_dict['commission_amount']
        return result, tot

    @property
    def commissions_amount(self):
        """ Total commission for the day """
        result, tot = self.commissions_vendor
        return tot

    @property
    def avg_commissions(self):
        """ Average commission peramount for the day """
        result, tot = self.commissions_vendor
        if len(self.items_price):
            return tot / len(self.items_price)
        return 0

    @property
    def iter_orders(self):
        """ For each order related to current report get amount of commission"""
        reports = self.prefetched_query.filter(
            create_at=self.create_at)
        orders = reports.first().orders.all()
        tot = 0
        for order in orders:
            order_total = order.items_price["total_amount"]["total_amount"]
            try:
                commission_rate = order.vendor.commission.rate
            except Exception as error:
                logger.error(
                    f"Error '{error}' while getting {order.vendor} commission")
                commission_rate = 0
            commission_amount = order_total * (commission_rate / 100)
            current = {
                "total_amount": order_total,
                "commission_rate": commission_rate,
                "commission_amount": commission_amount
            }
            tot += commission_amount
            yield order, current

    @property
    def commissions_items(self) -> Dict:
        """ Average commission amount per promotion for the day """
        result = defaultdict(list)
        for order, amount_dict in self.iter_orders:
            for item_id, item_price_dict in order.items_price["items"].items():
                order_total = item_price_dict["total_amount"]
                try:
                    commission_rate = order.vendor.commission.rate
                except Exception as error:
                    logger.error(
                        f"Error '{error}' while getting "
                        f"{order.vendor} commission")
                    commission_rate = 0
                commission_amount = order_total * (commission_rate / 100)
                current = {
                    "total_amount": order_total,
                    "commission_rate": commission_rate,
                    "commission_amount": commission_amount
                }
                result[item_price_dict["promotion"]].append(current)

        return result

    @property
    def commissions_promotions(self):
        """ Commission amount per promotion for the day """
        result = dict()
        for promotion, amount_dict in self.commissions_items.items():
            result[promotion] = sum(
                d["commission_amount"] for d in amount_dict
            )
        return result

    @property
    def commissions(self):
        """ Commission property """
        return {
            "promotion": self.commissions_promotions,
            "total": self.commissions_amount,
            "order_average": self.avg_commissions,
        }
