# myapp/models.py
from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class record(models.Model):
    name = models.CharField(max_length=100 ,default = 'sda')
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
