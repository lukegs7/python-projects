from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import JSONParser
from demo.models import UserEntity, FruitEntity, Category, Contact
from demo.serializers import UserEntitySerializer, FruitEntitySerializer, CategorySerializer, ContactSerializer


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
