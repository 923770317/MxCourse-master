# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from django.db.models import Q
from .models import BlogType,Blog,Comment
from  operation.models import UserFavorite,CourseComments, UserCourse
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from utils.mixin_utils import LoginRequireMixin


# Create your views here.

class BlogsListVies(View):

    def get(self,request):
        all_blogs = Blog.objects.all().order_by('-create_time')
        all_types = BlogType.objects.all()
        hot_blogs = Blog.objects.all().order_by('click_nums')[:3]

        #取出类别
        type = request.GET.get('type','')
        if type:
            all_blogs = all_blogs.filter(blog_type=type)

        # 关键词搜索功能
        search_keywords = request.GET.get('keywords','')
        if search_keywords:
            all_blogs = all_blogs.filter(Q(title__icontains=search_keywords) | Q(content__icontains=search_keywords))

        # 博客排序 默认是按时间倒叙，也可以按点击数
        sort = request.GET.get('sort','')
        if sort:
            if sort == 'hot':
                all_blogs = all_blogs.order_by('-click_nums')

        blog_nums = all_blogs.count()

        # 对博客进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_blogs, 3, request=request)
        blogs = p.page(page)

        return render(request, "blog-list1.html",
                      {"all_blogs": blogs,
                       "all_types": all_types,
                       "type": type,
                       "hot_blogs": hot_blogs,
                        "blog_nums":blog_nums,
                       "sort": sort})



# blog detail
class BlogDetailView(View):
    def get(self,request,blog_id):
        blog = Blog.objects.get(id=int(blog_id))
        blog.click_nums +=1
        blog.save()

        return render(request,'blog-detail.html',{
          'blog': blog,
        })



class CommentView(View):
    def post(self,request):
        if not request.user.is_authenticated():
            return HttpResponse('{"status": "fail", "msg":"用户未登录"}', content_type="application/json")

        blog_id = request.POST.get("id")
        content = request.POST.get("content")

        blog = Blog.objects.get(id=int(blog_id))
        comment = Comment()
        comment.blog = blog
        comment.content = content
        comment.author = request.user
        comment.save()
        return HttpResponse('{"status": "success", "msg":"评论成功"}', content_type="application/json")
