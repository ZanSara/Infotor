# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-21 17:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Percorso',
            fields=[
                ('IDperc', models.IntegerField(primary_key=True, serialize=False)),
                ('Nume', models.CharField(max_length=6)),
                ('Trek1', models.CharField(max_length=80)),
                ('Percorr', models.CharField(max_length=2)),
                ('Denomi', models.CharField(max_length=80)),
                ('PerLun', models.IntegerField()),
                ('PerLunF', models.IntegerField()),
                ('Perquo1', models.IntegerField()),
                ('Perquo2', models.IntegerField()),
                ('Pendenza', models.IntegerField()),
                ('PerTem1', models.IntegerField()),
                ('PerTem2', models.IntegerField()),
                ('PerDif', models.CharField(max_length=3)),
                ('Segni', models.CharField(max_length=3)),
                ('Dataril', models.DateField()),
                ('ReteReg', models.CharField(max_length=4)),
                ('CodReg', models.CharField(max_length=12)),
                ('Operatiore', models.CharField(max_length=80)),
                ('Storico', models.CharField(max_length=2)),
                ('Arcitett', models.CharField(max_length=2)),
                ('Paesagg', models.CharField(max_length=2)),
                ('Natural', models.CharField(max_length=2)),
                ('Link', models.CharField(max_length=16)),
                ('UTENTE', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Torrente',
            fields=[
                ('IDtrat', models.IntegerField(primary_key=True, serialize=False)),
                ('Trtname', models.CharField(max_length=16)),
                ('Regione', models.CharField(max_length=2)),
                ('Provincia', models.CharField(max_length=2)),
                ('Comune', models.CharField(max_length=6)),
                ('Grumon', models.CharField(max_length=11)),
                ('Sezion', models.CharField(max_length=7)),
                ('Nuovo', models.CharField(max_length=2)),
                ('Tipologia', models.CharField(max_length=2)),
                ('Caratter', models.CharField(max_length=2)),
                ('PerLun', models.IntegerField()),
                ('PerLunF', models.IntegerField()),
                ('Perquo1', models.IntegerField()),
                ('Perquo2', models.IntegerField()),
                ('Pendenza', models.IntegerField()),
                ('PerTem1', models.IntegerField()),
                ('PerTem2', models.IntegerField()),
                ('PerDif', models.CharField(max_length=3)),
                ('Dataril', models.DateField()),
                ('Rilevatore', models.CharField(max_length=50)),
                ('TipoRIL', models.CharField(max_length=3)),
            ],
        ),
    ]