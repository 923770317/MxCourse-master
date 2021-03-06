# coding:utf-8
"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,include
from django.contrib import admin

# TemplateView：专门用来处理静态文件,不需要专门写一个view来映射.
from django.views.generic import TemplateView
import xadmin
# django处理静态文件内容
from django.views.static import serve

from users.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView, RestView, ModifyPwdView, LogoutView, IndexView,AboutView
from organization.views import OrgView
from MxOnline.settings import MEDIA_ROOT, STATIC_ROOT

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', IndexView.as_view(), name="index"),
    # url(r'^login/$', TemplateView.as_view(template_name="login.html"), name="login"),
    # url(r'^login/$', user_login, name="login"),
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
    url(r'^register/$', RegisterView.as_view(), name="register"),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name="user_active"),
    url(r'^forget/$', ForgetPwdView.as_view(), name="forget_pwd"),
    url(r'^reset/(?P<reset_code>.*)/$', RestView.as_view(), name="reset_pwd"),
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name="modify_pwd"),
    url(r'^about/$', AboutView.as_view(), name="about"),

    # 课程机构URL配置
    url(r'^org/', include('organization.urls', namespace="org")),

    # 课程列表
    url(r'^course/', include('courses.urls', namespace="course")),

    # 博客
    url(r'^blogs/',include('blog.urls',namespace='blog')),

    # 新闻
    url(r'^news/',include('news.urls',namespace='news')),

    # 用户
    url(r'^users/', include('users.urls', namespace="users")),

    # 杂七杂吧
    url(r'^impurity/',include('impurity.urls',namespace='impurity')),

    # media的url配置，图片上传的url路径
    url(r'media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    # 当debug=False时，自行处理static内容
    url(r'static/(?P<path>.*)$', serve, {"document_root": STATIC_ROOT}),

    # 富文本相关url
    url(r'^ueditor/',include('DjangoUeditor.urls')),


] 


# 全局404
handler404 = 'users.views.page_no_found'

# 全局500
handler500 = 'users.views.page_error'

