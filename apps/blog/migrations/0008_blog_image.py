# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-12-05 23:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blog_brief'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog/%Y%m', verbose_name='\u535a\u5ba2\u63d2\u56fe'),
        ),
    ]