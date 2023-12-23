from django.core.signals import request_finished
from django.dispatch import receiver
from django.http import HttpRequest



@receiver(request_finished)
def update_reservation_status(sender, **kwargs):
    print("Site Loaded Successfully: ")