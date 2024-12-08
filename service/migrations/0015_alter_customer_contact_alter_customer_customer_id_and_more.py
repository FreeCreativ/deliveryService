# Generated by Django 5.1.3 on 2024-11-18 11:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0014_alter_review_options_alter_customer_customer_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='contact',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.CharField(default='Q9P3E1MX', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='expense_id',
            field=models.CharField(default='WF5SX115', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='customer', to='service.customer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='H14TIV7X', max_length=20, unique=True),
        ),
    ]
