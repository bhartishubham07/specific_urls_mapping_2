from App2.views import *
from django.urls import path

app_name ='Bittu'

urlpatterns = [
    path('first_App2/', first_App2, name='first_App2'),
    path('second_App2/', second_App2, name='second_App2'),
]
