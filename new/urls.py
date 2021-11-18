from django.urls import path
from .views import *

urlpatterns=[
    path('',home,name='home'),
    path('excel/',excel,name='excel'),
    path('view/',view,name='view'),
]