from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('shoes/',views.get_shoes ),
    path('shoe/',views.add_shoe),
]