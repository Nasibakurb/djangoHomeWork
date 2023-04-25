from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Здесь 3.2")

# Create your views here.
