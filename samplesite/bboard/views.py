import requests
from django.shortcuts import render


def users(request):
    response = requests.get('https://')
    data = response.json()
    users = data['users']
    context = {'users': users}
    return render(request, 'users.html', context)
