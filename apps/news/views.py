# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from django.db.models import Q
from .models import News,NewType,Sentence
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
import random


# Create your views here.

class NewsListViews(View):
    '''
    新闻列表
    '''
    def get(self,request):
        all_news = News.objects.all()
        all_types = NewType.objects.all()
        current_env = "news"

        # 随机每日一句
        randomInt = random.randint(0,Sentence.objects.all().count())
        try:
            sentence = Sentence.objects.get(id=randomInt)
        except Sentence.DoesNotExist:
            sentence = Sentence.objects.get(id=1)

        # 关键词
        search_keywords = request.GET.get('keywords','')
        if search_keywords:
            all_news = all_news.filter(title__icontains=search_keywords)

        sort = request.GET.get("sort","")
        if sort:
            if sort == 'time':
                all_news = all_news.order_by("-create_time")

        # 新闻排行榜
        sorted_news = News.objects.order_by('-click_nums')[:3]

        # 取出类别
        type = request.GET.get('type', '')
        if type:
            all_news = all_news.filter(type=type)

        # 对新闻进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
            # Provide Paginator with the request object for complete querystring generation

        news_count = all_news.count()
        p = Paginator(all_news, 3, request=request)
        all_news = p.page(page)
        return render(request,'new_news_list.html',{
            'all_news':all_news,
            'sorted_news':sorted_news,
            'sort':sort,
            'current_nav':current_env,
            'news_count':news_count,
            'all_types':all_types,
            'sentence':sentence,
        })


class NewDetailView(View):
    def get(self,request,id):
        new = News.objects.get(id= int(id))
        new.click_nums +=1
        new.save()

        return render(request, 'new_info.html', {
            'new': new,
        })
