from django.shortcuts import render
from firstweb.models import cal
# Create your views here.
from django.http.response import HttpResponse

def index(request):
    return render(request,'index.html')

def CalPage(request):
    return render(request,'cal.html')

def Cal(request):
    if request.method=="POST":
        valuea=request.POST['valueA']
        valueb=request.POST['valueB']
        print(valuea,valueb)
        cal.objects.create(value_a=valuea,value_b=valuea,result=int(valuea)+int(valueb))

        return render(request,'result.html',context={'data':int(valuea)+int(valueb)})
    else:
        return HttpResponse("please visit us with post")

def CalList(request):
    data=cal.objects.all()
    # for i in data:
        # print(i.value_a,i.value_b,i.result)
    return render(request,'table.html',context={"data":data})

def del_data(request):
    cal.objects.all().delete()
    return HttpResponse('data deleted')

def query(request):
    id=request.POST['id']
    return HttpResponse(f"id is {id}")