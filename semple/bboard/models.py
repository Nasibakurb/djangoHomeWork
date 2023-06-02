from django.db import models


class MyModel(models.Model):
    myModel1 = models.CharField(null=True, max_length=10)
    myModel2 = models.CharField(null=True, max_length=20)
    myModel3 = models.CharField(null=True, max_length=50)
    myModel4 = models.TextField(null=True, default=None)
    myModel5 = models.TextField(null=True, default=None)
