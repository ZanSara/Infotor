# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-16 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infotor', '0002_auto_20180416_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='torrente',
            name='Nuovo',
            field=models.CharField(choices=[('SI', 'Sì'), ('NO', 'No')], max_length=2, verbose_name='Nuovo tracciato?'),
        ),
    ]