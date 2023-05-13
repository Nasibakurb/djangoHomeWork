from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=15)
    work = models.BooleanField(default=True)
    age = models.PositiveIntegerField(max_length=110)


class Child(models.Model):
    parents = models.ForeignKey(Person, on_delete=models.CASCADE)
    name = models.CharField(max_length=15)
    age = models.PositiveIntegerField(max_length=12)
    study = models.BooleanField(default=True)


class Icecream(models.Model):
    size = models.CharField(max_length=50)
    type_ = models.CharField(max_length=40)
    price = models.FloatField(max_length=9999)


class IcecreamMarket(models.Model):
    ice_creams = models.ManyToManyField(Icecream)
    soze_building = models.CharField(max_length=10)
    description = models.CharField(max_length=2000)







