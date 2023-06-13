from django.db import models


class Order(models.Model):
    marketplace = models.CharField(max_length=100)
    idFlux = models.CharField(max_length=100)
    order_status_marketplace = models.CharField(max_length=100)
    order_status_lengow = models.CharField(max_length=100)
    order_id = models.CharField(max_length=100)
