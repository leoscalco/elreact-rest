# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 18:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_session', '0004_auto_20171113_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pathinstance',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address_point', to='address_session.Address'),
        ),
    ]
