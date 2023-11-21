from django.urls import path

from num.views import *

app_name = 'numbers'

urlpatterns = [
    path('one/',one,name='one'),
    path('two/',two,name='two'),
    path('three/',three,name='three'),
]