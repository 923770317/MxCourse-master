# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-26 22:17
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='\u6807\u9898')),
                ('content', models.TextField(default='', verbose_name='\u6b63\u6587')),
                ('create_time', models.DateTimeField(default=datetime.datetime(2018, 7, 26, 22, 17, 19, 950000), verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('click_nums', models.IntegerField(default=150, verbose_name='\u70b9\u51fb\u91cf')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237')),
                ('blog_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.BlogType', verbose_name='\u535a\u5ba2\u7c7b\u522b')),
            ],
            options={
                'verbose_name': '\u535a\u5ba2',
                'verbose_name_plural': '\u535a\u5ba2',
            },
        ),
    ]
