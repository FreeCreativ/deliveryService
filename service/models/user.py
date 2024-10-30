from django.contrib.auth.models import AbstractUser
from django.db import models

ROLE_CHOICES = (
    ('User', 'User'),
    ('Rider', 'Rider'),
    ('Staff', 'Staff'),
)
STATUS_CHOICES = (
    ('ACTIVE', 'Active'),
    ('PASSIVE', 'Passive'),
)


# Create your models here.
class User(AbstractUser):
    roles = models.CharField(choices=ROLE_CHOICES, default='User')


class Customer(models.Model):
    customer_id = models.CharField(max_length=25)
    name = models.TextField()
    phone = models.CharField(max_length=20, help_text='Phone Number')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
