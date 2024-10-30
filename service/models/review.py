from django.db import models

from service.models.user import Customer


class Review(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    review=models.TextField()
    date_created=models.DateTimeField(auto_now_add=True)
    date_modified=models.DateTimeField(auto_now=True)
