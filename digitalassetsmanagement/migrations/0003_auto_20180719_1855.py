# Generated by Django 2.0.5 on 2018-07-19 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digitalassetsmanagement', '0002_auto_20180719_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capture',
            name='title',
            field=models.CharField(default=' ', help_text='Ex.: The title of this record', max_length=256, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='item',
            name='title',
            field=models.CharField(default=' ', help_text='Ex.: The title of this record', max_length=256, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='thumbnail',
            name='title',
            field=models.CharField(default=' ', help_text='Ex.: The title of this record', max_length=256, verbose_name='Title'),
        ),
    ]
