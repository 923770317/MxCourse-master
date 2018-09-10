# coding:utf-8
from __future__ import unicode_literals

from django.utils import timezone
from django.db import models
from users.models import UserProfile
from DjangoUeditor.models import UEditorField

# Create your models here.


class BlogType(models.Model):
    '''
    博客类型
    '''
    name = models.CharField(max_length=10,verbose_name=u'博客类型')
    is_delete = models.BooleanField(default=False, verbose_name=u"是否删除")

    class Meta:
        verbose_name = u"博客类型"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Blog(models.Model):
    '''
    博客
    '''
    title = models.CharField(max_length=50, verbose_name=u'标题')
    content = UEditorField(verbose_name=u'正文', width=1200, height=600, imagePath='blog/ueditor/',
                           filePath='blog/ueditor/', default='')
    create_time = models.DateTimeField(verbose_name=u'创建时间', default=timezone.now)
    modify_time =  models.DateTimeField(verbose_name=u'创建时间', auto_now=True)
    click_nums = models.IntegerField(verbose_name=u'点击量', default=150)
    blog_type = models.ForeignKey(BlogType, verbose_name='博客类别',null=True,blank=True)
    blog_author = models.ForeignKey(UserProfile, verbose_name=u"作者", editable=False,null=True,blank=True)

    class Meta:
        verbose_name = u"博客"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    '''
     评论
    '''
    blog = models.ForeignKey(Blog, verbose_name=u'博客')
    content = models.TextField(verbose_name=u'评论内容')
    create_time = models.DateTimeField(verbose_name=u'创建时间', default=timezone.now)
    comment_author = models.ForeignKey(UserProfile, verbose_name=u"作者", editable=False,null=True,blank=True)

    class Meta:
        verbose_name = u"评论"
        verbose_name_plural = verbose_name
