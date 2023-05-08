from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.shipment_details_update),

]
