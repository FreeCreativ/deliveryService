import random
import string

from django.db import models

from business.models import Staff
from .customer import Customer


def generate_order_id():
    """Generate a random alphanumeric string of length 8 for the customerId"""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))


def switch_color(value):
    match value:
        case "Pending":
            return "yellow"
        case 'Processing':
            return "blue"
        case 'Delivered':
            return "green"
        case 'Cancelled':
            return "red"


class Order(models.Model):
    rider = models.ForeignKey(Staff, null=True, blank=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.CASCADE,
                                 related_query_name='customer')
    order_id = models.CharField(max_length=20, unique=True, default=generate_order_id())
    from_location = models.CharField(max_length=255)
    to_location = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_type = models.CharField(max_length=20)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, blank=True, null=True, default='Pending', choices=[
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ])

    @property
    def status_color(self):
        return switch_color(self.status)

    cancel_reason = models.CharField('reason', max_length=150, blank=True, null=True)

    def __str__(self):
        return f"Order {self.order_id} - {self.from_location} to {self.to_location}"

    class Meta:
        ordering = ('-order_date',)
