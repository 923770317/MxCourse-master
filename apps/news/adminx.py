# -*- coding: utf-8 -*-

# @File    : news register xadmin 呵呵
# @Date    : 2018-08-13
# @Author  : derek.zhang

import xadmin
from .models import News

class NewsAdmin(object):
    list_display = ['title',  'author', 'create_time','is_banner', 'click_nums',]
    search_fields = ['title', 'content']
    list_filter = ['author', 'create_time','is_banner']
    style_fields = {'content': 'ueditor'}

    def save_models(self):
        '''
        实现保存当前用户
        '''
        obj = self.new_obj
        request = self.request
        obj.author = request.user
        obj.save()


xadmin.site.register(News,NewsAdmin)