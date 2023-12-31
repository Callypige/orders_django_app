# Generated by Django 4.2.2 on 2023-06-13 12:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='idFlux',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_status_lengow',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_status_marketplace',
        ),
        migrations.AddField(
            model_name='order',
            name='order_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='order',
            name='order_currency',
            field=models.CharField(default='EUR', max_length=10),
        ),
        migrations.AddField(
            model_name='order',
            name='order_purchase_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
