# -*- coding: utf-8 -*-

# @File    : impurity 路由配置
# @Date    : 2019-01-03
# @Author  : derek.zhang


from django.conf.urls import url,include
from .views import *

urlpatterns = [
    url(r'^list/$', GoodsListView.as_view(), name="goods_list"),
    # # 新闻详情
    # url(r'^new/detail/(?P<id>\d+)/$', NewDetailView.as_view(), name="new_detail"),
]