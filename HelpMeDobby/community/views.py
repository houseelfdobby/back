from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('test')

def create(request):
    return HttpResponse('test') 

def detail(request,pk):
    return HttpResponse('test')

def delete(request,pk):
    return HttpResponse('test')

def edit(request,pk):
    return HttpResponse('test')