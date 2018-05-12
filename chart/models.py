from django.db import models

#from numpy.random import random_sample

# Create your models here.

class Tempvalt(models.Model):
    temperature = models.FileField()
    altitude = models.IntegerField()