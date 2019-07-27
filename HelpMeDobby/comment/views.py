from django.shortcuts import render, HttpResponse

# Create your views here.

# CUD

def create(request):
    return HttpResponse('test')

# ajax 
def edit(request,pk):
    return HttpResponse('test')

def delete(request,pk):
    return HttpResponse('test')