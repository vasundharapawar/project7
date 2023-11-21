from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def a(request):
    return render(request,'a.html')

def e(request):
    return HttpResponse('<h1>This is E function HttpResponse </h1>')

def i(request):
    return HttpResponse('<h1>This is I function httpresponse</h1>')