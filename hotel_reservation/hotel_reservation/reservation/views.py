from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from main.models import Hotel
from .models import Reservation

# Create your views here.
def add_reservation_view(request, hotel_id):
    if request.user.is_authenticated:
        hotel = Hotel.objects.get(pk=hotel_id)
        user = User.objects.get(pk=request.user.id)
        
        if request.method == "POST":
            schedule = request.POST.get('schedule')
            reservation = Reservation(user=user, reserved_hotel=hotel, schedule=schedule)
            hotel.reservation_status = "RS"
            hotel.save()
            reservation.save()

            return redirect(reverse('hotels'))

        return render(request, 'reservation/add_reservation.html', {'hotel':hotel})
    else:
        pass

def my_reservation_view(request):
    if request.user.is_authenticated:
        user = User.objects.get(pk=request.user.id)
        reservations = Reservation.objects.filter(user=user, )
        return render(request, 'reservation/my_reservation.html', {'reservations':reservations})
    else:
        return render(request, 'main/redirect.html')

def reschedule_reservation_view(request, hotel_id):
    hotel = Hotel.objects.get(pk=hotel_id)
    reservation = Reservation.objects.get(reserved_hotel=hotel)

    rescheduled = True
    if request.method == "POST":
        schedule = request.POST.get('schedule')
        reservation.schedule = schedule
        reservation.save()

        return redirect(reverse('hotels'))

    return render(request, 'reservation/add_reservation.html', {'hotel':hotel, 'rescheduled':rescheduled, 'reservation':reservation})
    
    
def pay_now_view(request, reservation_id):
    reservation = Reservation.objects.get(pk=reservation_id)
    reservation.paid = True
    reservation.save()

    return redirect(reverse('add_reservation'))


def check_out_view(request, reservation_id):
    reservation = Reservation.objects.get(pk=reservation_id)

    hotel = Hotel.objects.get(pk=reservation.reserved_hotel.id)
    hotel.reservation_status = "AV"
    
    reservation.checkout = True

    hotel.save()
    reservation.save()

    return redirect(reverse('my_reservation'))