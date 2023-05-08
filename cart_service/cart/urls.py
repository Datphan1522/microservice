from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('cart/<int:product_id>', views.add_to_cart),
    # path('cart/delete/<int:cart_id>',views.deleteCartItem),
    path('cart/<int:cart_id>',views.add_to_cart),
    path('cart/',views.get_cart_items),

    # path('shipment_updates/', views.shipment_reg_update)
]
