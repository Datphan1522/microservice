from __future__ import unicode_literals
from django.db import models

# Create your models here.
# -*- coding: utf-8 -*-

from django.db import models


# model của book
class Shoe(models.Model):
    # The following are the fields of our table.
    shoe_id = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    availability = models.CharField(max_length=15)
    price = models.IntegerField()
    quantity = models.IntegerField()
    brand = models.CharField(max_length=200)
    description = models.TextField()
    size = models.IntegerField()


    # # It will help to print the values.
    # def __str__(self):
    #     return '%s %s %s %s %s' % (self.product_id, self.product_category,
    #                                self.product_name, self.availability, self.price)
