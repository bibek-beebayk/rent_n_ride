from types import BuiltinMethodType, CoroutineType
from django.db import models
from django.contrib.auth.models import User
import uuid

from django.db.models.deletion import SET_NULL


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    province = models.CharField(max_length=20, choices = [
        # ('Province 1', 'Province 1'),
        # ('Madhesh', 'Madhesh'),
        ('Bagmati', 'Bagmati'),
        # ('Gandaki', 'Gandaki'),
        # ('Lumbini', 'Lumbini'),
        # ('Karnali', 'Karnali'),
        # ('Sudurpaschim', 'Sudurpaschim'),
    ], null=True)
    city = models.CharField(max_length=100, null=True)
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=10, choices=[
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ], null=True)
    email = models.EmailField(max_length=500, null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    short_intro = models.CharField(max_length=300, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(
        null=True, blank=True, upload_to='users/', default='users/user-default.png ')
    # social_facebook = models.CharField(max_length=200, null=True, blank=True)
    # social_github = models.CharField(max_length=200, null=True, blank=True)
    # social_twitter = models.CharField(max_length=200, null=True, blank=True)
    # social_linkedin = models.CharField(max_length=200, null=True, blank=True)
    # social_youtube = models.CharField(max_length=200, null=True, blank=True)
    # social_website = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self) -> str:
        return str(self.username)

class UserReview(models.Model):
    CHOICE = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    user = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.CASCADE)
    review_text = models.TextField(null=True, blank=True)
    review_rating = models.CharField(max_length=1, choices=CHOICE)
    created = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    sender = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True)
    receiver = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name='messages')
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.subject

    class Meta:
        ordering = ['is_read', '-created']