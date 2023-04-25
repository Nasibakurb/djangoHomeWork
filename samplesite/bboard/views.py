from django.shortcuts import render

from django.http import HttpResponse
def index(request):
    return HttpResponse("Здесь 4.2")
# Create your views here.
