# Generated by Django 2.0.1 on 2018-04-26 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_orderwarehouse'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrderShipmentTruck',
        ),
        migrations.DeleteModel(
            name='Warehouse',
        ),
    ]