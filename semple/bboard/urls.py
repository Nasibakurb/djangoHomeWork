from django.urls import path, re_path
from .views import SMSListView, create_sms, delete_sms, read_sms, get_sms, my_view

urlpatterns = [
    path('', SMSListView.as_view(), name='sms_list'),
    # re_path(r^$', SMSListView.as_view(), name='sms_list'),

    path('create/', create_sms, name='create_sms'),
    # re_path(r'create/$', create_sms, name='create_sms'),

    path('delete/<int:sms_id>/', delete_sms, name='delete_sms'),
    # re_path(r'delete/(?P<sms_id>\d+)/$', delete_sms, name='delete_sms'),

    path('sms/<int:sms_id>/', read_sms, name='sms_read'),
    # re_path(r'sms/(?P<sms_id>\d+)/$', read_sms, name='sms_read'),

    path('get/<int:sms_id>/', get_sms, name='get_sms'),
    # re_path(r'get/$', get_sms, name='get_sms')

    path('view/', my_view, name='view')
]



