# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-12-04 23:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_delete_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='brief',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='\u7b80\u4ecb'),
        ),
    ]