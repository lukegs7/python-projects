#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/17 7:16 下午
# @Author  : lukegs7
# @File    : urls.py
# @Software: PyCharm

from django.urls import include, path
from rest_framework import routers
from comment.views import CommentViewSet

router = routers.DefaultRouter()
router.register('comment', CommentViewSet)

urlpatterns = [
    path('', include(router.urls))
]
