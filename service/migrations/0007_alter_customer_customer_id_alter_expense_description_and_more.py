# Generated by Django 5.1.3 on 2024-11-15 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0006_alter_customer_customer_id_alter_expense_expense_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.CharField(default='JTT6CMB6', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='expense_id',
            field=models.CharField(default='R4SFHSEF', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='F6B3EP1B', max_length=20, unique=True),
        ),
    ]
