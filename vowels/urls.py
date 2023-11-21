from django.urls import path

from vowels.views import *

app_name = 'vowels'

urlpatterns = [
    path('a/',a,name='a'),
    path('e/',e,name='e'),
    path('i/',i,name='i'),
]