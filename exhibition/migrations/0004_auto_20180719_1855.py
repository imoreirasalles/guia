# Generated by Django 2.0.5 on 2018-07-19 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibition', '0003_auto_20180719_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibition',
            name='title',
            field=models.CharField(default=' ', help_text='Ex.: The title of this record', max_length=256, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='exhibitionedition',
            name='title',
            field=models.CharField(default=' ', help_text='Ex.: The title of this record', max_length=256, verbose_name='Title'),
        ),
    ]