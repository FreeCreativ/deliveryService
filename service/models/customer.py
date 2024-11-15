import random
import string

from django.db import models
from django.db.models import Sum, Count, Max, Q


def generate_id():
    """Generate a random alphanumeric string of length 8 for the customerId"""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))


class Customer(models.Model):
    customer_id = models.CharField(max_length=20, unique=True, default=generate_id())
    customer_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    joined = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, blank=True, null=True)

    def get_order_summary(self):
        """
        Fetch and cache aggregated order information in a single query to optimize for fewer DB calls.
        """
        order_summary = self.order_set.aggregate(
            cancelled_count=Count('id', filter=Q(status='Cancelled')),
            total_count=Count('id'),
            last_order_date=Max('order_date'),
            total_amount=Sum('amount')
        )

        # Store the aggregated values in instance attributes to avoid repeated DB calls
        self._cancelled_orders = order_summary['cancelled_count']
        self._order_count = order_summary['total_count']
        self._last_order_date = order_summary['last_order_date']
        self._amount = order_summary['total_amount'] or 0

    def cancelled_orders(self):
        if not hasattr(self, '_cancelled_orders'):
            self.get_order_summary()
        return self._cancelled_orders

    def order_count(self):
        if not hasattr(self, '_order_count'):
            self.get_order_summary()
        return self._order_count

    def last_order_date(self):
        if not hasattr(self, '_last_order_date'):
            self.get_order_summary()
        return self._last_order_date

    def amount(self):
        if not hasattr(self, '_amount'):
            self.get_order_summary()
        return self._amount

    def __str__(self):
        return f'self.customer_name'


class Review(models.Model):
    customer = models.CharField(max_length=150)
    review = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Review by {self.customer} on {self.date}'
