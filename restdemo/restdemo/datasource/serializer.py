#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/21 10:44 下午
# @Author  : lukegs7
# @File    : serializer.py
# @Software: PyCharm

from rest_framework import serializers
from datasource.models import *


class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = '__all__'


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'


class Node1Serializer(serializers.ModelSerializer):
    # module = ModuleSerializer(many=True)
    module_count=serializers.SerializerMethodField()

    def get_module_count(self, obj):
        data=Node.objects.annotate(module=Count())

    class Meta:
        model = Node
        fields = '__all__'
