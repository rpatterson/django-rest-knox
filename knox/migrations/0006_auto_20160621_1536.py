# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knox', '0005_authtoken_encrypted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authtoken',
            name='encrypted',
            field=models.CharField(max_length=184, null=True),
        ),
    ]
