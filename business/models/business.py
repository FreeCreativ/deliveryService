from django.db import models


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

    class Meta:
        verbose_name_plural = 'business setting'


class Business(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    company_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=128)
