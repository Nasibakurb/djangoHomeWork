import requests
from django.shortcuts import render


def index(requests):
    return render(requests, "index.html")

def contact (request):
    return render(request, "contact.html")

def galler(request):
    return render(request, "galler.html")

def sign(request):
    return render(request, "sign_in.html")
