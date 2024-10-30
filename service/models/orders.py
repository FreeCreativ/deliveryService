from django.conf import settings
from django.db import models

from service.models.user import Customer


class Order(models.Model):
    STATUS_CHOICES = [
        ('CREATED', 'Created'),
        ('IN_TRANSIT', 'In Transit'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    ]

    PRIORITY_CHOICES = [
        ('STANDARD', 'Standard'),
        ('EXPRESS', 'Express'),
        ('URGENT', 'Urgent'),
    ]
    TYPE_CHOICES = [
        ('PICKUP', 'Pickup'),
        ('ERRAND', 'Errand'),
        ('WAYBILL', 'Waybill'),
    ]

    # user = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.CASCADE,
    #     related_name='logistics_orders'
    # )
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer')
    order_number = models.CharField(max_length=20, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='CREATED')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='STANDARD')
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='PICKUP')
    origin = models.CharField('from', max_length=255)
    destination = models.CharField('to', max_length=255)
    estimated_delivery_date = models.DateField(null=True, blank=True)
    actual_delivery_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Logistics Order {self.order_number} - {self.get_status_display()}"


class Shipment(models.Model):
    order = models.ForeignKey(Order, related_name='shipments', on_delete=models.CASCADE)
    tracking_number = models.CharField(max_length=50, unique=True)
    carrier = models.CharField(max_length=100)
    departure_date = models.DateTimeField()
    arrival_date = models.DateTimeField(null=True, blank=True)
    current_location = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=20, choices=Order.STATUS_CHOICES, default='IN_TRANSIT')

    def __str__(self):
        return f"Shipment {self.tracking_number} - {self.get_status_display()}"


class Package(models.Model):
    shipment = models.ForeignKey(Shipment, related_name='packages', on_delete=models.CASCADE)
    package_id = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2, help_text="Weight in kilograms")
    dimensions = models.CharField(max_length=100, help_text="L x W x H in cm")

    def __str__(self):
        return f"Package {self.package_id} - {self.description[:20]}"
