from django.urls import path

from conso.views import *

app_name = 'consonants'

urlpatterns = [
    path('b/',b,name='b'),
    path('c/',c,name='c'),
    path('z/',z,name='z'),
]