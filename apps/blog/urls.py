# coding:utf-8

from django.conf.urls import url, include
from .views import BlogsListVies,BlogDetailView,CommentAddView

urlpatterns = [
    url(r'^list/$', BlogsListVies.as_view(), name="blog_list"),
    url(r'^detail/(?P<blog_id>\d+)/$', BlogDetailView.as_view(), name="blog_detail"),
    url(r'^addComment/$', CommentAddView.as_view(), name="add_comment"),
]