# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 15:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0003_auto_20171118_1132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='related',
            name='article_a',
        ),
        migrations.RemoveField(
            model_name='related',
            name='article_b',
        ),
        migrations.DeleteModel(
            name='Related',
        ),
    ]