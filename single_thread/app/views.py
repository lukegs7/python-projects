from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def func(request):
    count = 0
    while True:
        if count % 100 == 0:
            print(count)
        count += 1
    return HttpResponse('not ok')


def func1(request):
    return HttpResponse('hello world!')
