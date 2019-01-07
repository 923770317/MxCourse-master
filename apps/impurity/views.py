# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic.base import View
from.models import Goods,ShareType
import random
from news.models import Sentence
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

class GoodsListView(View):
    '''
    分享列表
    '''

    def get(self,request):
        all_goods = Goods.objects.all()
        all_types = ShareType.objects.all()

        # 随机每日一句
        randomInt = random.randint(0, Sentence.objects.all().count())
        try:
            sentence = Sentence.objects.get(id=randomInt)
        except Sentence.DoesNotExist:
            sentence = Sentence.objects.get(id=1)

        # 关键词搜索
        search_keywords = request.GET.get('keywords','')
        if search_keywords:
            all_goods = all_goods.filter(title__icontains=search_keywords)

        # 取出类别
        type = request.GET.get('type','')
        if type:
            all_goods = all_goods.filter(type = type)

        goods_num = all_goods.count()

        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_goods, 20, request=request)
        goods = p.page(page)

        return render(request, "share.html",
                      {"all_goods": goods,
                       "all_types": all_types,
                       'sentence': sentence,
                       'goods_num': goods_num,
                       })


class GoodDetailView(View):
    '''
    分享详情
    '''
    def get(self,request,good_id):
        good = Goods.objects.get(id=int(good_id))
        good.view_nums += 1
        good.save()
        return render(request,'good_detail.html',{
           'good':good,
        })
