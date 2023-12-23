from django import forms
from .models import Hotel


class AddHotel(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = [
            "name",
            "address",
            "price",
            "reservation_status",
            "img_url"
        ]

    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    price = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    reservation_status = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    img_url = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control'}))