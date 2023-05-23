from django.db import models


class MyModel(models.Model):
    myList = models.CharField(blank=True, default=None, max_length=40)

