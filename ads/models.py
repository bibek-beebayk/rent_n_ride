from django.db import models
from django.core.validators import RegexValidator
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
    engine_capacity = models.PositiveSmallIntegerField(verbose_name='Engine capacity in CC', null=True, blank=True)
    distance_travelled = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True)
    registration_number = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        validators= [RegexValidator(r'[a-zA-Z]+([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[eE]([+-]?\d+))?-[a-zA-Z]+([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[eE]([+-]?\d+))?')],
        help_text= ("Eg: BA-2-CH-1234"),
        )
    is_available = models.BooleanField(default=True)
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