from django.db import models

from business.models import Staff
from .customer import Customer


class Order(models.Model):
    rider = models.ForeignKey(Staff, on_delete=models.CASCADE, related_query_name='rider')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_query_name='customer')
    order_id = models.CharField(max_length=20, unique=True)
    from_location = models.CharField(max_length=255)
    to_location = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_type = models.CharField(max_length=50)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ])
    cancel_reason = models.CharField('reason', max_length=150, blank=True, null=True)

    def __str__(self):
        return self.order_id
