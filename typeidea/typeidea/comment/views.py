from django.http import JsonResponse
from django.shortcuts import redirect
from django.utils import timezone
from django.views.generic import TemplateView, View

from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from comment.models import Comment
from comment.serializer import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    parser_classes = (JSONParser,)
