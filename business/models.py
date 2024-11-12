from django.db import models
from django.db.models import Sum


class Staff(models.Model):
    ROLE_CHOICES = (
        ('User', 'User'),
        ('Rider', 'Rider'),
        ('Staff', 'Staff'),
    )
    profile_image = models.ImageField(upload_to='images/profileImage')
    staff_id = models.CharField(max_length=20)
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
    bank_name = models.CharField(max_length=50)
    account_number = models.CharField(max_length=255)
    account_name = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=100, blank=True, null=True)
    vehicle_reg_number = models.CharField(max_length=100, blank=True, null=True)
    insurance_details = models.CharField(max_length=255, blank=True, null=True)
    driver_license = models.CharField(max_length=100, blank=True, null=True)
    staff_agreement = models.FileField(upload_to='documents/staff_agreements/')
    verification_document = models.FileField(upload_to='documents/verification_documents/')

    def total_earning(self):
        # This will return the total amount as a number, or 0 if there are no orders
        total = self.order_set.aggregate(total_amount=Sum('amount'))['total_amount']
        return total or 0  # Return 0 if total is None (e.g., no orders)

    def __str__(self):
        return self.name


class BusinessSetting(models.Model):
    business_name = models.CharField(max_length=255)
    started_date = models.DateField()
    logo = models.ImageField(upload_to='business_logos/')
    currency = models.CharField(max_length=10)
    currency_symbol_placement = models.CharField(max_length=10,
                                                 choices=[('Before', 'Before Amount'), ('After', 'After Amount')])
    business_email = models.EmailField()
    business_phone = models.CharField(max_length=20)
    business_country = models.CharField(max_length=100)
    business_state = models.CharField(max_length=100)
    business_address = models.TextField()

    def __str__(self):
        return self.business_name


class Activity(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
