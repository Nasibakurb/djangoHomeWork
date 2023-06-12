from django.db import models
from django.http import JsonResponse
class SMS(models.Model):
    sender = models.CharField(max_length=100, verbose_name='Отправитель')
    receiver = models.CharField(max_length=100, verbose_name='Получатель')
    message = models.TextField(verbose_name='Сообщение')
    created_at = models.DateTimeField(auto_now_add=True)

