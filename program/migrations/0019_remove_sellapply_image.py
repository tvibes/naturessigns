# Generated by Django 2.2.4 on 2020-06-22 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0018_sellapply_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sellapply',
            name='image',
        ),
    ]