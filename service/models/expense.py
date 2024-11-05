from django.db import models


class Expense(models.Model):
    exp_id = models.CharField(max_length=20, unique=True)
    category = models.CharField(max_length=50)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    vendor = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=50, choices=[
        ('Cash', 'Cash'),
        ('Bank Transfer', 'Bank Transfer'),
        ('Card', 'Card'),
    ])
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('Paid', 'Paid'),
        ('Pending', 'Pending'),
        ('Reimbursed', 'Reimbursed'),
    ])

    def __str__(self):
        return self.exp_id
