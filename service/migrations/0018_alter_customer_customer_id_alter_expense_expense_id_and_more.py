# Generated by Django 5.1.3 on 2024-11-18 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0017_alter_customer_customer_id_alter_customer_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.CharField(default='O5SWGYJX', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='expense_id',
            field=models.CharField(default='AH73A50E', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='JVQAM48L', max_length=20, unique=True),
        ),
    ]
