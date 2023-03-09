from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def first_App2(request):
    return HttpResponse('<marquee><h1>THIS IS FIRST FUNCTION OF APP2</h1></marquee>')

def second_App2(request):
    return HttpResponse('<marquee><h1>THIS IS THE SECOND FUNCTION OF APP2</h1></marquee>')
