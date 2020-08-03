from django.shortcuts import render

# Create your views here.
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count
from datasource.models import *
from datasource.serializer import *


class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
    parser_classes = (JSONParser,)


class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    parser_classes = (JSONParser,)


@api_view(['GET'])
def node_list(request):
    nodes = Node.objects.annotate(module_count=Count('module')).all()
    serialzier = Node1Serializer(nodes)
    return Response(serialzier.data)


@api_view(['GET'])
def get_nodes(request):
    nodes = Node.objects.all().prefetch_related('module').all()
    serializer = NodeSerializer(nodes,many=True)
    return Response(serializer.data)
