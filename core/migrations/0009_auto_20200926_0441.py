# Generated by Django 3.0.8 on 2020-09-26 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20200926_0241'),
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
