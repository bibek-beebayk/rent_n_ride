from django.db import models
import uuid
# Create your models here.

class VehicleMake(models.Model):
    make = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.make

class Vehicle(models.Model):
    VEHICLE_CHOICES = [
        ('C', 'Car'),
        ('M', 'Motrobike'),
        ('B', 'Bicycle'),
        ('O', 'Other')
    ] 

    type = models.CharField(max_length=1, choices=VEHICLE_CHOICES, null=True)
    make = models.ForeignKey(VehicleMake, on_delete=models.PROTECT, null=True)
    model = models.CharField(max_length=200, null=True)
    distance_travelled = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    registration_number = models.CharField(max_length=100, null=True, blank=True)
    # owner = 
    # related_ad = 
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    image = models.ImageField(blank=True, null=True, upload_to='vehicles', default='vehicles/vehicle-default.jpg')

    def __str__(self) -> str:
        return str(self.make) + ' ' + self.model



