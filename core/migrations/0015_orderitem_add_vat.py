# Generated by Django 3.0.8 on 2020-09-27 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_remove_item_add_vat'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='add_vat',
            field=models.BooleanField(default=False),
        ),
    ]
