from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def b(request):
    return render(request,'b.html')

def c(request):
    return HttpResponse('<h1>This is C function from consonants..</h1>')

def z(request):
    return HttpResponse('<h1>this is z function from consonants</h1>')