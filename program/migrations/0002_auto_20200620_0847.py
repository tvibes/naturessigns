# Generated by Django 2.2.4 on 2020-06-20 08:47

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partnerjoin',
            name='country',
            field=django_countries.fields.CountryField(default='select country', max_length=2),
        ),
    ]
