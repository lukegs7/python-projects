#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/15 11:58 下午
# @Author  : lukegs7
# @File    : serializers.py
# @Software: PyCharm

from rest_framework import serializers
from .models import *

class UserEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEntity
        fields = '__all__'


class FruitEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = FruitEntity
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class DetectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detector
        fields = '__all__'
