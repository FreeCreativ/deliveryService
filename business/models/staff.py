from django.db import models
from django.db.models import Sum

from utils import generate_id


class Staff(models.Model):
    ROLE_CHOICES = (
        ('User', 'User'),
        ('Rider', 'Rider'),
        ('Staff', 'Staff'),
    )
    profile_image = models.ImageField(upload_to='images/profileImage', blank=True, null=True)
    staff_id = models.CharField(max_length=20, unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    state_of_origin = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    emergency_contact = models.CharField(max_length=15)
    start_date = models.DateField()
    position = models.CharField(max_length=100)
    pay_rate = models.DecimalField(max_digits=10, decimal_places=2)
    bank_details = models.TextField()
    # bank_name = models.CharField(max_length=50)
    # account_number = models.CharField(max_length=255)
    # account_name = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=100, blank=True, null=True)
    vehicle_reg_number = models.CharField(max_length=100, blank=True, null=True)
    insurance_details = models.CharField(max_length=255, blank=True, null=True)
    driver_license = models.CharField(max_length=100, blank=True, null=True)
    staff_agreement = models.FileField(upload_to='documents/staff_agreements/', blank=True, null=True)
    verification_document = models.FileField(upload_to='documents/verification_documents/', blank=True, null=True)

    @property
    def total_earning(self):
        # This will return the total amount as a number, or 0 if there are no orders
        total = self.order_set.aggregate(total_amount=Sum('amount'))['total_amount']
        return total or 0  # Return 0 if total is None (e.g., no orders)

    @property
    def total_expenses(self):
        # This will return the total amount as a number, or 0 if there are no expenses
        total = self.expense_set.aggregate(total_amount=Sum('amount'))['total_amount']
        return total or 0  # Return 0 if total is None (e.g., no expenses)

    @property
    def total_trips(self):
        return self.order_set.count()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:  # Only set a new value on creation
            self.staff_id = generate_id()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Staff'





class Activity(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
