# -*- coding: utf-8 -*-

# @File    : nwes 路由配置 呵呵
# @Date    : 2018-08-13
# @Author  : derek.zhang

from django.conf.urls import url,include
from .views import *

urlpatterns = [
    url(r'^list/$', NewsListViews.as_view(), name="news_list"),
    # 新闻详情
    url(r'^new/detail/(?P<id>\d+)/$', NewDetailView.as_view(), name="new_detail"),
]