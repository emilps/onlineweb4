# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-09 20:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posters', '0005_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermixin',
            name='order_type',
            field=models.IntegerField(choices=[(1, 'Plakat'), (2, 'Bong'), (3, 'Annet')]),
        ),
    ]