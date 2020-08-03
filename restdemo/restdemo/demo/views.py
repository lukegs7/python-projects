from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import JSONParser
from .models import UserEntity, FruitEntity, Category, Contact, Detector
from .serializers import UserEntitySerializer, FruitEntitySerializer, CategorySerializer, ContactSerializer, \
    DetectorSerializer
from rest_framework.decorators import api_view


class UserViewSet(ModelViewSet):
    queryset = UserEntity.objects.all()
    serializer_class = UserEntitySerializer
    parser_classes = (JSONParser,)


class FruitViewSet(ModelViewSet):
    queryset = FruitEntity.objects.all()
    serializer_class = FruitEntitySerializer
    parser_classes = (JSONParser,)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    parser_classes = (JSONParser,)


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    parser_classes = (JSONParser,)


@api_view(['GET'])
def get_modules(request):
    """
        返回所有依赖关系
        结果内容：
        {
            'user': [
                { 'name':'geshuai','contact':[1,2] }
            ],
            'contact':
                {
                    1:'address',
                    2:'address'
                }
        }
    :return:
    """
    res = {'code': 0, 'msg': 'success', 'data': []}
    query_result = UserEntity.objects.select_related('contact').all()
    users = []
    contacts = {}
    for item in query_result:
        users.append(item.contact.id)
        contacts[item.contact.id] = item.contact.address
    data = {'users': users, 'contacts': contacts}
    res['data'] = data
    return JsonResponse(res)


class DetectorViewSet(ModelViewSet):
    queryset = Detector.objects.all()
    serializer_class = DetectorSerializer
    parser_classes = (JSONParser,)
