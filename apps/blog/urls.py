# coding:utf-8

from django.conf.urls import url, include
from .views import BlogsListVies,BlogDetailView

urlpatterns = [
    url(r'^list/$', BlogsListVies.as_view(), name="blog_list"),
    url(r'^detail/(?P<blog_id>\d+)/$', BlogDetailView.as_view(), name="blog_detail"),
]