from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def News(request):
    return HttpResponse('Hello')
