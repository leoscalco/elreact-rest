# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 16:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_session', '0002_auto_20171113_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='path',
            field=models.ManyToManyField(related_name='path', through='user_session.PathInstance', to='address_session.Address'),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='residentialAddress',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='residential', to='address_session.Address'),
        ),
    ]
