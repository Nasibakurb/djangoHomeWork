from django.urls import path
from bboard.views import home, users

urlpatterns = [
    path('', home, name='home'),
    path('users/', users, name='users'),
]
