from __future__ import unicode_literals

from datetime import date

from django.shortcuts import render

# Create your views here.
# -*- coding: utf-8 -*-
from django.http import HttpResponse

from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from book_model.models import Book


def insert_book(barcode,title,author,category,publisher,publication_date,availability,price,description,quantity):
    book_data = Book(barcode=barcode,title=title,book_category=category,author=author,publisher=publisher,publication_date=publication_date,quantity=quantity,availability=availability,description=description,price=price)
    book_data.save()
    return 1


@csrf_exempt
def get_books(request):
    data = []
    resp = {}
    insert_book('112211', 'sach hay', 'Abc', 'sach', 'Ha Noi', '2022-09-11', 'avialable', '120', 'sach hay',
                45)
    # This will fetch the data from the database.
    prodata = Book.objects.all()
    for tbl_value in prodata.values():
        data.append(tbl_value)
    # If data is available then it returns the data.
    if data:
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['data'] = data
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Data is not available.'
    return HttpResponse(json.dumps(resp,cls=DateEncoder), content_type='application/json')


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.strftime('%d-%m-%Y')
        return super().default(obj)

