# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    price = models.IntegerField(max_length=1000)


class Order(models.Model):
    name= models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    order = models.CharField(max_length=1150)