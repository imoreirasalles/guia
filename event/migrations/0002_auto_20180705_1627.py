# Generated by Django 2.0.5 on 2018-07-05 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eventtype',
            options={'verbose_name': 'Event Type', 'verbose_name_plural': 'Events Type'},
        ),
    ]
