# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-12 09:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newbeginnings', '0021_auto_20170812_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='exchange_offer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exchange_post', to='newbeginnings.Post'),
        ),
    ]
