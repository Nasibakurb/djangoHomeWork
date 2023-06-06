from django.urls import path
from .views import SMSListView, create_sms, delete_sms

urlpatterns = [
    path('create/', create_sms, name='create_sms'),
    path('', SMSListView.as_view(), name='sms_list'),
    path('sms/delete/<int:sms_id>/', delete_sms, name='delete_sms'),

]



