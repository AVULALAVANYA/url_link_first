from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def wish(request):
    return HttpResponse('<marquee><h1>wish me on november</h1></marquee>')

def lavanya(request):
    return HttpResponse('<marquee><b>lavanya birthday</b></marquee>')