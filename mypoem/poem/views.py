from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from . import service
from django.urls import reverse
def index(request):
    # 1. 获得数据
    poems=service.getAllPoems()
    # 2. render渲染首页
    return render(request,'index.html',{'poems': poems})

def detail(request,id):
    poem=service.getPoem(id)
    return render(request,'detail.html',{'poem': poem})

def add(request):
    return render(request,'add.html',{})

def svc_add(request):
    # 1. 获得form提交的数据，通过POST
    title=request.POST['title']
    content=request.POST['content']
    # 2. 将数据提交到数据库
    service.addPoem(title,content)
    # 3. 重定向到首页
    # 模板中的{% url %}标签的功能与reverse的功能是一致的
    return HttpResponseRedirect(reverse('poem:index'))

def delete(request,id):
    # 根据id在数据库中删除诗歌，重定向到首页
    service.deletePoem(id)
    return HttpResponseRedirect(reverse('poem:index'))

def edit(request,id):
    # 获得要修改的诗歌
    poem=service.getPoem(id)
    # 渲染修改页面
    return render(request,'edit.html',{'poem':poem})

def svc_edit(request,id):
    # 获得修改后的title和content
    # 提交id title content数据到service去修改
    title=request.POST['title']
    content = request.POST['content']
    service.editPoem(id,title,content)
    return HttpResponseRedirect(reverse('poem:index'))