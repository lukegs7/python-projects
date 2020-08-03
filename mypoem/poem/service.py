#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/24 9:45 下午
# @Author  : lukegs7
# @File    : service.py
# @Software: PyCharm


from .models import Poem

def getAllPoems():
    return Poem.objects.all()

def getPoem(id):
    return Poem.objects.get(pk=id)

def addPoem(title,content):
    Poem.objects.create(title=title,content=content)

def deletePoem(id):
    poem=Poem.objects.get(pk=id)
    poem.delete()

def editPoem(id,title,content):
    poem=Poem.objects.get(pk=id)
    poem.title=title
    poem.content=content
    poem.save()