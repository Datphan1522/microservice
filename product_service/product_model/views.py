from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
# -*- coding: utf-8 -*-
from django.http import HttpResponse

from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from product_model.models import product_details

def insert_product(product_id,product_category,product_name,availability,price):
    product_data = product_details(product_id=product_id,product_category=product_category,product_name=product_name,availability=availability,price=price)
    product_data.save()
    return 1

@csrf_exempt
def get_product_data(request):
    data = []
    resp = {}

    insert_product('123123','sach','sach khoa hoc va doi song','avialable',60)
    
    # This will fetch the data from the database.
    prodata = product_details.objects.all()
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
    return HttpResponse(json.dumps(resp), content_type = 'application/json')