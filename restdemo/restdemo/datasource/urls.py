#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/21 10:48 下午
# @Author  : lukegs7
# @File    : urls.py
# @Software: PyCharm

from django.urls import path,include
from rest_framework import routers
from datasource.views import *

router=routers.DefaultRouter()
router.register('node',NodeViewSet)
router.register('module',ModuleViewSet)

urlpatterns=[
    path('',include(router.urls)),
    path('node_list/',node_list),
    path('values/',get_nodes)
]