#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/16 7:42 上午
# @Author  : lukegs7
# @File    : urls.py
# @Software: PyCharm

from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('fruit', FruitViewSet)
router.register('contact', ContactViewSet)
router.register('category', CategoryViewSet)
router.register('detector',DetectorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/',get_modules)
]
