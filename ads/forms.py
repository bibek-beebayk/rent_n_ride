from django import forms
from .models import Ad, AdReview

class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['ad_title', 'vehicle_type', 'vehicle_make', 'model', 'distance_travelled', 'registration_number', 'is_available','location', 'asking_price', 'featured_image', 'description']

class AdReviewForm(forms.ModelForm):
    class Meta:
        model = AdReview
        fields = ['review_text', 'review_rating']

class AdSearchForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['vehicle_type', 'vehicle_make', 'model', 'distance_travelled', 'location', 'asking_price']