from django.forms import ModelForm
from .models import Profile, Message

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'username', 'province', 'city', 'location', 'date_of_birth', 'gender', 'email', 'phone', 'short_intro', 'bio', 'profile_image']

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'body']