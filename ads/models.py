from django.db import models
import uuid
from users.models import Profile
# Create your models here.


class VehicleMake(models.Model):
    make = models.CharField(max_length=100, null=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.make


class Ad(models.Model):

    VEHICLE_CHOICES = [
        ('C', 'Car'),
        ('M', 'Motrobike'),
        ('B', 'Bicycle'),
        ('S', 'Scooter'),
        ('O', 'Other')
    ]

    ad_title = models.CharField(max_length=200, null=True)
    owner = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.SET_NULL)
    vehicle_type = models.CharField(
        max_length=1, choices=VEHICLE_CHOICES, null=True)
    vehicle_make = models.ForeignKey(
        VehicleMake, on_delete=models.PROTECT, null=True)
    model = models.CharField(max_length=200, null=True)
    distance_travelled = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True)
    registration_number = models.CharField(
        max_length=100, null=True, blank=True)
    available_from = models.DateField(null=True)
    available_till = models.DateField(null=True)
    location = models.CharField(max_length=200, null=True)
    asking_price = models.DecimalField(
        max_digits=8, decimal_places=2, null=True)
    featured_image = models.ImageField(
        blank=True, null=True, upload_to='ads/', default='ads/ad-default.jpg')
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.ad_title

    class Meta:
        ordering = ['-created']


class AdReview(models.Model):
    CHOICE = [
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ]
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    ad = models.ForeignKey(Ad, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, null = True, on_delete= models.CASCADE)
    review_text = models.TextField(null=True, blank=True)
    review_rating = models.CharField(max_length=1, choices=CHOICE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [['ad', 'user']]

    def __str__(self) -> str:
        return str(self.user) + str(self.ad) + self.review_rating + self.review_text