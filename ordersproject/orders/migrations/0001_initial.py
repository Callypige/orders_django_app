# Generated by Django 4.2.2 on 2023-06-13 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marketplace', models.CharField(max_length=100)),
                ('idFlux', models.CharField(max_length=100)),
                ('order_status_marketplace', models.CharField(max_length=100)),
                ('order_status_lengow', models.CharField(max_length=100)),
                ('order_id', models.CharField(max_length=100)),
            ],
        ),
    ]
