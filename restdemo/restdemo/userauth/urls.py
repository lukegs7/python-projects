#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/1 10:48 下午
# @Author  : lukegs7
# @File    : urls.py
# @Software: PyCharm

from django.urls import path, include
from .views import *

urlpatterns = [
    path('v2/login/',ProLoginView.as_view()),
    path('v2/user/info/',UserInfo.as_view())
]
