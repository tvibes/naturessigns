# Generated by Django 2.2.4 on 2020-06-20 08:56

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0003_partnerjoin_zip_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partnerjoin',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
