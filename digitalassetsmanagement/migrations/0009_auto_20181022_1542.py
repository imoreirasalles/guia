# Generated by Django 2.0.5 on 2018-10-22 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digitalassetsmanagement', '0008_auto_20180802_1518'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='capture',
            options={'verbose_name': 'Image', 'verbose_name_plural': 'Images'},
        ),
    ]