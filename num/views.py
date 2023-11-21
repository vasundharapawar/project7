from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def one(request):
    return render(request,'one.html')

def two(request):
    return HttpResponse('<h1>This is two function from numbers app</h1>')

def three(request):
    return HttpResponse('<h1>This is three function from numbers app</h1>')
