
from django import forms
from .models import Vehicle

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['type', 'make', 'model', 'distance_travelled', 'registration_number', 'description', 'image']