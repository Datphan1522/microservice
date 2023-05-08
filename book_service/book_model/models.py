from __future__ import unicode_literals
from django.db import models

# Create your models here.
# -*- coding: utf-8 -*-

from django.db import models


# model của book
class Book(models.Model):
    # The following are the fields of our table.
    barcode = models.CharField(max_length=200)
    book_category = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    availability = models.CharField(max_length=15)
    price = models.CharField(max_length=15)
    quantity = models.IntegerField()
    author = models.CharField(max_length=200)
    description = models.TextField()
    publisher = models.CharField(max_length=200)
    publication_date = models.DateField();


    # # It will help to print the values.
    # def __str__(self):
    #     return '%s %s %s %s %s' % (self.product_id, self.product_category,
    #                                self.product_name, self.availability, self.price)
