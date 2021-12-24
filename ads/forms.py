
from django import forms
from .models import Ad

class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['ad_title','owner', 'vehicle_type', 'vehicle_make', 'model', 'distance_travelled', 'registration_number', 'available_from', 'available_till','location', 'asking_price', 'featured_image', 'description']