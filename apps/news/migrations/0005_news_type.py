# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-12-10 22:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_news_brief'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='type',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='\u65b0\u95fb\u7c7b\u578b'),
        ),
    ]
