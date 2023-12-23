from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_hotel/', views.add_hotel_view, name='add_hotel'),
    path('hotels/', views.hotel_view, name='hotels')
]