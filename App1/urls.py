from App1.views import *
from django.urls import path

app_name ='Shubham'

urlpatterns = [
    path('first_App1/', first_App1, name='first_App1'),
    path('second_App1/', second_App1, name='second_App1'),
]
