from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('room/<str:pk>/', views.rooms, name='room'),
    path('cart/', views.cart, name="cart")
]
