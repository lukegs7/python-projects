#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/1 10:48 下午
# @Author  : lukegs7
# @File    : urls.py
# @Software: PyCharm

from django.urls import path, include
from api.views import AuthView,OrderView,ProOrderView,ProLoginView

urlpatterns = [
    path('v1/auth/', AuthView.as_view()),
    path('v1/order/',ProOrderView.as_view()),
    path('v1/login/',ProLoginView.as_view()),
    path('v1/user/info/',ProOrderView.as_view()),
]
