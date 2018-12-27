# coding:utf-8
from __future__ import unicode_literals

from django.utils import timezone
from django.db import models
from users.models import UserProfile
from DjangoUeditor.models import UEditorField
# Create your models here.


class NewType(models.Model):
    '''
    新闻类型
    '''
    name = models.CharField(max_length=10,verbose_name=u'新闻类型')
    is_delete = models.BooleanField(default=False, verbose_name=u"是否删除")

    class Meta:
        verbose_name = u"新闻类型"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Sentence(models.Model):
    '''
    每日一句
    '''
    content = models.CharField(max_length=150, verbose_name=u'每日一句')

    class Meta:
        verbose_name = u'每日一句'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.content



class News(models.Model):
    '''
     新闻
    '''
    title = models.CharField(max_length=50,verbose_name=u'标题')
    type = models.ForeignKey(NewType,verbose_name=u"新闻类型", null=True, blank=True)
    author = models.ForeignKey(UserProfile, verbose_name=u"作者", editable=False)
    create_time = models.DateTimeField(verbose_name=u'发布时间', default=timezone.now)
    click_nums = models.IntegerField(verbose_name=u'点击量', default=150)
    content = UEditorField(verbose_name=u'新闻内容', width=1200, height=600, imagePath='blog/ueditor/',
                           filePath='blog/ueditor/', default='')
    is_banner = models.BooleanField(default=False, verbose_name=u"是否轮播")
    image = models.ImageField(max_length=100, upload_to='news/%Y%m', verbose_name=u"轮播图", blank=True, null=True)
    brief = models.CharField(max_length=50, verbose_name=u'简介',null= True,blank=True)
    class Meta:
        verbose_name = u"新闻"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title