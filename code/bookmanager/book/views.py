from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    context={'title':'测试木块处理数据'}
    return render(request,'Book/index.html',context)
