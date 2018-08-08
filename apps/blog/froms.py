# -*- coding: utf-8 -*-

# @File    : 呵呵
# @Date    : 2018-08-08
# @Author  : derek.zhang


import re
from django import forms
from blog.models import Comment

# 使用modelform编写表单
class CommentAddForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content",""]
