# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-26 22:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u521b\u5efa\u65f6\u95f4'),
        ),
    ]
