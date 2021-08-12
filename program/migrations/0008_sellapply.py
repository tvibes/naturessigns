# Generated by Django 2.2.4 on 2020-06-21 15:30

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0007_auto_20200620_1321'),
    ]

    operations = [
        migrations.CreateModel(
            name='SellApply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=19, null=True)),
                ('country_of_citizenship', django_countries.fields.CountryField(max_length=2)),
                ('country_of_residence', django_countries.fields.CountryField(max_length=2)),
                ('product_name', models.CharField(max_length=120)),
                ('manufacturer', models.CharField(blank=True, max_length=120)),
                ('product_origin', django_countries.fields.CountryField(max_length=2)),
                ('product_sku', models.CharField(blank=True, max_length=120)),
                ('product_description', models.TextField(max_length=1500)),
                ('selling_price', models.DecimalField(decimal_places=2, default=None, max_digits=19)),
                ('date_produced', models.DateField()),
                ('expiry_date', models.DateField()),
                ('image', models.ImageField(default=None, null=True, upload_to='')),
            ],
        ),
    ]
