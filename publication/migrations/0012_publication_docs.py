# Generated by Django 2.0.5 on 2018-11-28 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digitalassetsmanagement', '0010_auto_20181128_0014'),
        ('publication', '0011_publication_is_draft'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='docs',
            field=models.ManyToManyField(blank=True, to='digitalassetsmanagement.Doc', verbose_name='Documents'),
        ),
    ]
