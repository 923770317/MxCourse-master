# -*- coding: utf-8 -*-

# @File    : impurity 路由配置
# @Date    : 2019-01-03
# @Author  : derek.zhang


from django.conf.urls import url,include
from .views import *

urlpatterns = [
    # 分享列表
    url(r'^list/$', GoodsListView.as_view(), name="goods_list"),

    # 分享详情
    url(r'^detail/(?P<good_id>\d+)/$', GoodDetailView.as_view(), name="good_detail"),
]