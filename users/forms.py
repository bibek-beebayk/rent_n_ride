from django.forms import ModelForm
from .models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'username', 'location', 'date_of_birth', 'gender', 'email', 'phone', 'short_intro', 'bio', 'profile_image']