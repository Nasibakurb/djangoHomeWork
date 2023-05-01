from django.urls import path
from bboard.views import index, contact, galler,sign

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('galler/', galler, name='galler'),
    path('sign/', sign, name='sign'),
]
