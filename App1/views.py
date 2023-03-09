from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def first_App1(request):
    return HttpResponse('<h1>THIS IS THE FIRST FUNCTION OF APP1</h1>')

def second_App1(request):
    return HttpResponse('<h1>THIS IS THE SECOND FUNCTION OF APP1</h1>')