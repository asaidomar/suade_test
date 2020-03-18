from typing import List, Dict

from django.db import models
from django.utils.functional import cached_property


class Report(models.Model):
    """ Report model """
    create_at = models.DateField()
    orders = models.ManyToManyField("orders.Order")

    @property
    def prefetched_query(self):
        return Report.objects.prefetch_related(
            "orders__customer",
            "orders__items__product",
            "orders__items__discount",
            "orders__vendor__commission",
        )

    @property
    def items(self):
        """ Items for day self.create_at """
        return self.prefetched_query.filter(
            create_at=self.create_at).values("orders__items__quantity")

    @property
    def items_count(self):
        """ Items count for day self.create_at """
        return sum(i["orders__items__quantity"] for i in self.items)

    @property
    def consumers(self):
        """ Consumer for the day create_at """
        return self.prefetched_query.filter(
            create_at=self.create_at).values("orders__customer__id")

    @property
    def consumer_count(self):
        """ Consumer Count for the day create_at """
        return self.consumers.count()

    @cached_property   # instance cached
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

        tot = sum(d["orders__items__quantity"] for d in discounts)
        rates = sum(
            d["orders__items__quantity"] * d["orders__items__discount__rate"]
            for d in discounts
        )
        return rates / tot

    @property
    def avg_order_total(self):
        """ The average order total for the day create_at """
        total = sum([
            i["total_amount"]["total_amount"] for i in self.items_price
        ])
        n_order = len(self.items_price)
        return total/n_order
