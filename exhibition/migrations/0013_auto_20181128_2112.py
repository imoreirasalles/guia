# Generated by Django 2.0.5 on 2018-11-28 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0006_auto_20180802_1518'),
        ('exhibition', '0012_exhibition_audience'),
    ]

    operations = [
        migrations.AddField(
            model_name='exhibition',
            name='locations',
            field=models.ManyToManyField(help_text='What is the exhibition edition location?', to='location.Location', verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='exhibition',
            name='location',
            field=models.ForeignKey(blank=True, help_text='What is the exhibition edition location?', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='old_location', to='location.Location', verbose_name='Location'),
        ),
    ]
