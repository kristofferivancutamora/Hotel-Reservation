from django.shortcuts import render
from .forms import AddHotel
from django.http.response import HttpResponse
from .models import Hotel

# Create your views here.
def home(request):
    return render(request, 'main/index.html')


def add_hotel_view(request):
    if request.method == "POST":
        form = AddHotel(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponse("Record Added Successfully")
    else:
        form = AddHotel
        return render(request, 'main/add_hotel.html', {'form': form})

def hotel_view(request):
    hotels = Hotel.objects.all()

    return render(request, 'main/hotels.html', {'hotels':hotels})
