# Generated by Django 3.0.8 on 2020-09-27 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_orderitem_add_vat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='add_vat',
        ),
        migrations.AddField(
            model_name='item',
            name='add_vat',
            field=models.BooleanField(default=False),
        ),
    ]
