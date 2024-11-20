from django.db import models

from business.models import Staff
from utils import generate_id


def switch_color(value):
    match value:
        case "Paid'":
            return "green"
        case 'Pending':
            return "yellow"
        case 'Reimbursed':
            return "red"


class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('Fuel', 'Fuel'),
        ('Maintenance', 'Maintenance'),
        ('Packaging', 'Packaging'),
        ('Ticket', 'Ticket'),
        ('Rider', 'Rider Fee'),
        ('Others', 'Others'),
    ]
    staff = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, blank=True)
    expense_id = models.CharField(max_length=20, unique=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    vendor = models.CharField(max_length=255, blank=True, null=True)
    payment_method = models.CharField(max_length=50, blank=True, null=True, default='Cash', choices=[
        ('Cash', 'Cash'),
        ('Bank Transfer', 'Bank Transfer'),
        ('Card', 'Card'),
    ])
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending', blank=True, null=True, choices=[
        ('Paid', 'Paid'),
        ('Pending', 'Pending'),
        ('Reimbursed', 'Reimbursed'),
    ])

    @property
    def status_color(self):
        return switch_color(self.status)

    def save(self, *args, **kwargs):
        if not self.pk:  # Only set a new value on creation
            self.expense_id = generate_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.expense_id

    class Meta:
        ordering = ('-date',)
