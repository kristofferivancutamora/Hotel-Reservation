from django.db import models

# Create your models here.
class Hotel(models.Model):
    RESERVED = "RS"
    AVAILABLE = "AV"
    RESERVATION_STATUS_CHOICES = {
        RESERVED:"Reserved",
        AVAILABLE:"Available"
    }

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=500, null=True)
    img_url = models.ImageField(upload_to="images", null=True)
    reservation_status = models.CharField(max_length=2, choices=RESERVATION_STATUS_CHOICES, default=AVAILABLE)