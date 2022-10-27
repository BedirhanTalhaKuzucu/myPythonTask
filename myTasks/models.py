from inspect import iscode
from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=50)
    idNummer = models.IntegerField(blank=True, null=True)
    iscode = models.CharField(max_length=5)


    def __str__(self):
        return self.name
