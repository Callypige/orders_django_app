# Generated by Django 4.2.2 on 2023-06-13 13:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_order_idflux_remove_order_order_status_lengow_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_purchase_date',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
    ]
