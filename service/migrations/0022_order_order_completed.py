# Generated by Django 5.1.3 on 2024-11-19 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0021_alter_customer_customer_id_alter_expense_expense_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_completed',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
