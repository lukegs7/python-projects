#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/17 7:14 下午
# @Author  : lukegs7
# @File    : serializer.py
# @Software: PyCharm

from rest_framework import serializers
from comment.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
