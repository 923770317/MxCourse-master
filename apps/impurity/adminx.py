#/usr/bin/python
# -*- coding: utf-8 -*-

# @File    : xadmin 后台配置
# @Date    : 2019-01-03
# @Author  : derek.zhang

import  xadmin
from .models import ShareType,Goods

class ShareTypeAdmin(object):
    list_display = ['name', 'is_delete']
    search_fields = ['name']


class GoodsAdmin(object):
    list_display = ['title','type','is_free','url']
    search_fields = ['title','type','is_free']
    list_filter = ['type', 'is_free']


xadmin.site.register(ShareType,ShareTypeAdmin)
xadmin.site.register(Goods,GoodsAdmin)
