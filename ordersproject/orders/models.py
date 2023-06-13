from django.db import models
import datetime


class Order(models.Model):
    order_id = models.CharField(max_length=100)
    marketplace = models.CharField(max_length=100)
    order_purchase_date = models.DateField(
        default=datetime.date.today, null=True
    )
    order_currency = models.CharField(max_length=10, default="EUR")
    order_amount = models.DecimalField(
        max_digits=10, decimal_places=2, default=0
    )
