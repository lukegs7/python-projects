from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from .extensions.jwt_auth import create_token
from django.contrib import auth


class ProLoginView(APIView):
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        user = request.data.get('username')
        pwd = request.data.get('password')
        # user_object = User.objects.filter(username=user, password=pwd).first()
        user_object = auth.authenticate(username=user, password=pwd)
        print('user-object', user_object)
        if not user_object:
            return Response({'code': 1000, 'msg': '用户名或密码错误'})
        token = create_token({'id': str(user_object.id), 'name': user_object.username})
        return Response({'code': 20000, 'data': {'token': token}})


class UserInfo(APIView):
    def get(self, request, *args, **kwargs):
        print(request.user, request.GET)
        user_info = auth.models.User.objects.filter(username=request.user['name']).first()
        if user_info.is_superuser:
            roles = ['admin']
        else:
            roles = ['normal']
        data = {
            "roles": roles,
            "avatar": "",
            "name": user_info.first_name + user_info.last_name,
            "introduction": ""
        }
        return Response({'code': 20000, 'data': data})
