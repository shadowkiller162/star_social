# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-27 09:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='description_html',
        ),
    ]
