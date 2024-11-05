from django.db import models


class Customer(models.Model):
    customer_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    status = models.CharField(max_length=10)
    orders_count = models.IntegerField(default=0)
    last_order_date = models.DateField(null=True, blank=True)
    amount_spent = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Review(models.Model):
    customer_name = models.CharField(max_length=150)
    review = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Review by {self.customer_name} on {self.date}'
