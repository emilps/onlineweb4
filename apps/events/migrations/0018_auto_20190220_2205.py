# Generated by Django 2.0.13 on 2019-02-20 21:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0017_auto_20180221_2200'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'permissions': (('view_event', 'View Event'),), 'verbose_name': 'arrangement', 'verbose_name_plural': 'arrangementer'},
        ),
        migrations.AlterField(
            model_name='event',
            name='event_type',
            field=models.SmallIntegerField(choices=[(1, 'Sosialt'), (2, 'Bedriftspresentasjon'), (3, 'Kurs'), (4, 'Utflukt'), (5, 'Ekskursjon'), (6, 'Internt'), (7, 'Annet'), (8, 'Realfagskjelleren')], verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='event',
            name='ingress',
            field=models.TextField(help_text='En ingress som blir vist før beskrivelsen.', validators=[django.core.validators.MinLengthValidator(25)], verbose_name='ingress'),
        ),
        migrations.AlterField(
            model_name='event',
            name='ingress_short',
            field=models.CharField(help_text='En kort ingress som blir vist på forsiden', max_length=150, validators=[django.core.validators.MinLengthValidator(25)], verbose_name='kort ingress'),
        ),
        migrations.AlterField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.Group', verbose_name='arrangør'),
        ),
        migrations.AlterField(
            model_name='fieldofstudyrule',
            name='field_of_study',
            field=models.SmallIntegerField(choices=[(0, 'Gjest'), (1, 'Bachelor i Informatikk'), (10, 'Programvaresystemer'), (11, 'Databaser og søk'), (12, 'Algoritmer og datamaskiner'), (13, 'Spillteknologi'), (14, 'Kunstig intelligens'), (15, 'Helseinformatikk'), (16, 'Interaksjonsdesign, spill- og læringsteknologi'), (30, 'Annen mastergrad'), (40, 'Sosialt medlem'), (80, 'PhD'), (90, 'International'), (100, 'Annet Onlinemedlem')], verbose_name='studieretning'),
        ),
    ]
