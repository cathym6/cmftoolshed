"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Sports(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    description = models.CharField(max_length=500) 

class Skills(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    description = models.CharField(max_length=500)


class Description(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=800)

