# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-01-07 21:47
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('impurity', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sharetype',
            options={'verbose_name': '\u5206\u4eab\u7c7b\u578b', 'verbose_name_plural': '\u5206\u4eab\u7c7b\u578b'},
        ),
        migrations.AddField(
            model_name='goods',
            name='brief',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='\u7b80\u4ecb'),
        ),
        migrations.AddField(
            model_name='goods',
            name='content',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='\u6b63\u6587'),
        ),
    ]