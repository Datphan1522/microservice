from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from cart.models import CartItem
from django.views.decorators.http import require_http_methods
def get_cart_item(cart_id,prodct_id):
    products = CartItem.objects.filter(cart_id=cart_id,product_id=prodct_id)
    return products.first()

def data_insert(cart_id,price,quantity,product_id):
    cart_item = CartItem(cart_id=cart_id,price=price,quantity=quantity,product_id=product_id)
    cart_item.save()
    return 1

@csrf_exempt
@require_http_methods(['POST'])
def add_to_cart(request,cart_id):

    if request.method == 'POST':
        resp ={}

        if 'application/json' in request.META['CONTENT_TYPE']:
            val = json.loads(request.body)

            product_id = val.get('product_id')
            quantity = val.get('quantity')
            price = val.get('price')

            if cart_id and quantity and price and product_id :
                respdata = get_cart_item(cart_id,product_id)
                if respdata :
                    respdata.quantity += quantity
                    respdata.save()
                    resp['status'] = 'Success'
                    resp['status_code'] = '200'
                    resp['message'] = 'Them Thanh Cong'
                else:
                    if data_insert(cart_id,price,quantity,product_id) :
                        resp['status'] = 'Success'
                        resp['status_code'] = '200'
                        resp['message'] = 'Them Thanh Cong'
                    else:
                        resp['status'] = 'Failed'
                        resp['status_code'] = '400'
                        resp['message'] = 'Them That Bai'
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'Thieu Truong Thong Tin'
        return HttpResponse(json.dumps(resp), content_type='application/json')

@csrf_exempt

def get_cart_items(request):
    data = []
    resp = {}
    # This will fetch the data from the database.
    cart_items = CartItem.objects.all()
    for tbl_value in cart_items.values():
        data.append(tbl_value)
    # If data is available then it returns the data.
    if data:
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['data'] = data
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Khong Co Du Lieu'
    return HttpResponse(json.dumps(resp), content_type='application/json')

@csrf_exempt
# @require_http_methods(['DELETE'])
def deleteCartItem(request, cart_id):
    resp = {}

    respdata = CartItem.objects.get(cart_id=id)
    respdata.delete()
    resp['status'] = 'Failed'
    resp['status_code'] = '400'
    resp['message'] = 'Them That Bai'
    return HttpResponse(json.dumps(resp), content_type='application/json')
