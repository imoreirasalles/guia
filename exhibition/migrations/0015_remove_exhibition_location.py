# Generated by Django 2.0.5 on 2018-11-28 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exhibition', '0014_location_migrate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exhibition',
            name='location',
        ),
    ]