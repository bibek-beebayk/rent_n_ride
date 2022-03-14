
from django import forms
from .models import Request

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['title','vehicle_type', 'location', 'start_date','end_date', 'description', 'image', 'offered_price',]