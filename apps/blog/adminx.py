#/usr/bin/python
#coding:utf-8

import xadmin
from .models import BlogType,Blog

class BlogTypeAdmin(object):
    list_display = ['name','is_delete']
    search_fields = ['name']


class BlogAdmin(object):
    list_display = ['title','blog_type','author','create_time','modify_time']
    search_fields = ['title']
    list_filter = ['blog_type','author']
    style_fields = {'content':'ueditor'}

    def save_models(self):
        '''
        实现保存当前用户
        '''
        obj = self.new_obj
        request = self.request
        obj.author = request.user
        obj.save()

    def queryset(self):
        '''
        实现数据的自动分离
        '''
        qs = super(BlogAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs
        else:
            return qs.filter(author = self.request.user)



xadmin.site.register(BlogType,BlogTypeAdmin)
xadmin.site.register(Blog,BlogAdmin)
