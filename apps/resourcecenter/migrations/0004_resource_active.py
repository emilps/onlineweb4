# Generated by Django 2.0.13 on 2019-05-04 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resourcecenter', '0003_auto_20190428_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]