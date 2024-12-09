# Generated by Django 5.1.3 on 2024-11-21 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0023_alter_customer_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('Cash', 'Cash'), ('Transfer', 'Transfer'), ('POS', 'POS')], default='Cash', max_length=20, null=True),
        ),
    ]
