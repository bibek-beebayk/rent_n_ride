from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH

# Create your models here.

class Request(models.Model):
    # owner = 
    title = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=200, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    vehicle_description: models.TextField(null=True)
    image = models.ImageField(blank=True, null=True, upload_to='images/requests', default='images/requests/request-default.jpg')
    offered_price = models.DecimalField(max_digits=8, decimal_places=2, null=True)

