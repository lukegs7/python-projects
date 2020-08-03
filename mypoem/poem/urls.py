#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/24 9:20 下午
# @Author  : lukegs7
# @File    : urls.py
# @Software: PyCharm

from django.urls import path
from . import views

# 重要
app_name='poem'

urlpatterns=[
    path('',views.index,name='index'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('add',views.add,name='add'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('svc_add',views.svc_add,name='svc_add'),
    path('svc_edit/<int:id>',views.svc_edit,name='svc_edit')
]

