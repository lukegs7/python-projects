from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
import traceback
from django.http import JsonResponse
from rest_framework.response import Response
from api.models import *
from .extensions.jwt_auth import create_token
from datetime import datetime
import jwt
from jwt import exceptions

# Create your views here.
ORDER_DICT = {
    1: {
        'name': '护手霜',
        'age': 18,
        'gender': '男',
        'content': '...'
    },
    2: {
        'name': '防晒shaun过',
        'age': 20,
        'gender': '男',
        'content': '...'
    },
}


def md5(user):
    import hashlib
    import time
    ctime = str(time.time())
    m = hashlib.md5(bytes(user, encoding='utf-8'))
    m.update(bytes(ctime, encoding='utf-8'))
    return m.hexdigest()


class Authication():
    pass


class OrderView(APIView):
    # 用于订单相关业务,必须登录成功或者登录过了才能获取
    # 前端请求带时候带了token则表示已经登录过
    # 应用认证规则
    authication_class = [Authication, ]

    def get(self, request, *args, **kwargs):
        self.dispatch()
        ret = {'code': 1000, 'msg': None}
        try:
            ret['data'] = ORDER_DICT
        except Exception as ex:
            pass
        return JsonResponse(ret)


class AuthView(APIView):
    """
        用于用户登录认证
    """

    def post(self, request, *args, **kwargs):
        ret = {'code': 1000, 'msg': None}
        try:
            import json
            params = request.data
            user = params['username']
            pwd = params['password']
            print(user, pwd)
            obj = UserInfo.objects.filter(username=user, password=pwd).first()
            if not obj:
                ret['code'] = 1002
                ret['msg'] = "用户名或密码错误"
            # 每次登录创建一个token
            token = md5(user)
            UserToken.objects.update_or_create(user=obj, defaults={'token': token})
            ret['token'] = token
        except Exception as ex:
            traceback.print_exc()
            pass
        return JsonResponse(ret)


class ProLoginView(APIView):
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        user = request.data.get('username')
        pwd = request.data.get('password')
        user_object = UserInfo.objects.filter(username=user, password=pwd).first()
        print(type(user_object.id), type(user_object.username))
        if not user_object:
            return Response({'code': 1000, 'msg': '用户名或密码错误'})
        token = create_token({'id': str(user_object.id), 'name': user_object.username})
        return Response({'code': 20000, 'data': {'token': token}})


# 订单视图
class ProOrderView(APIView):
    def get(self, request, *args, **kwargs):
        print(request.user, request.GET)
        return Response({'code': 20000, 'data': {
            "roles": ['admin'],
            "introduction": 'I am a super administrator',
            "avatar": 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
            "name": 'Super Admin'
        }})
