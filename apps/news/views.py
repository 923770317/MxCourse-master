# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from django.db.models import Q
from .models import News
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

class NewsListViews(View):
    def get(self,request):
        pass

