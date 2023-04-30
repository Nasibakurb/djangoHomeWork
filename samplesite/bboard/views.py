import requests
from django.shortcuts import render


def users(request):
    return render(request, "users.html")

def home(request):
    return render(request, "home.html")

