from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def posts_create(request):
    return HttpResponse("<h1>Create World</h1>")

def posts_detail(request):
    return HttpResponse("<h1>Detail World</h1>")

def posts_list(request):
    return HttpResponse("<h1>List World</h1>")

def posts_update(request):
    return HttpResponse("<h1>Update World</h1>")

def posts_delete(request):
    return HttpResponse("<h1>Delete World</h1>")

