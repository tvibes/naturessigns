# Generated by Django 3.0.8 on 2020-09-27 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_order_add_tax'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='add_tax',
        ),
    ]