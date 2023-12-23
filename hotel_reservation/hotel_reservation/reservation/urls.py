from django.urls import path
from . import views

urlpatterns = [
    path('add_reservation/<hotel_id>/', views.add_reservation_view, name='add_reservation'),
    path('my_reservation/', views.my_reservation_view, name='my_reservation'),
    path('reschedule_reservation/<hotel_id>/', views.reschedule_reservation_view, name='reschedule_reservation'),
    path('pay_now/<reservation_id>/', views.pay_now_view, name='pay_now'),
    path('checkout/<reservation_id>/', views.check_out_view, name='checkout'),

]