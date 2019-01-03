# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.db import models


# Create your models here.
class ShareType(models.Model):
    '''
    分享类型
    '''

    name = models.CharField(max_length=10,verbose_name=u'分享类型')
    is_delete = models.BooleanField(default=False, verbose_name=u"是否删除")

    class Meta:
        verbose_name = u"博客类型"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Goods(models.Model):
    '''
    分享实物，可以是电子书，可以是视频，可以是框架
    '''
    title = models.CharField(max_length=50,verbose_name=u'名称')
    type = models.ForeignKey(ShareType, verbose_name=u'分享类型')
    url = models.CharField(max_length=100, verbose_name=u'链接地址', null=True, blank=True)
    image = models.ImageField(max_length=100, upload_to='impurity/%Y%m', verbose_name=u"资源插图", blank=True, null=True)
    is_free = models.BooleanField(default=True,verbose_name='是否免费')

    class Meta:
        verbose_name = u"分享资源"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title