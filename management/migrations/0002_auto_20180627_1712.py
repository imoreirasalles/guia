# Generated by Django 2.0.5 on 2018-06-27 20:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='managementunit',
            options={'verbose_name_plural': 'Coordenações'},
        ),
        migrations.AddField(
            model_name='managementunit',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
