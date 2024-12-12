from django.db import models

from business.models import Staff
from utils import generate_id
from .customer import Customer


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
    customer = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.SET_NULL,
                                 related_query_name='customer')
    order_id = models.CharField(max_length=20, unique=True)
    from_location = models.CharField(max_length=255)
    to_location = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_type = models.CharField(max_length=20)
    order_date = models.DateTimeField(auto_now_add=True)
    order_completed = models.DateTimeField(auto_now=True)
    payment_method = models.CharField(max_length=20, default='Cash', blank=True, null=True, choices=[
        ('Cash', 'Cash'),
        ('Transfer', 'Transfer'),
        ('POS', 'POS')
    ])
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

    def save(self, *args, **kwargs):
        if not self.pk:  # Only set a new value on creation
            self.order_id = generate_id()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('-order_date',)
