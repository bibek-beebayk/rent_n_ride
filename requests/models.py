from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH
import uuid

# Create your models here.

class Request(models.Model):
    # owner = 
    title = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=200, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    description= models.TextField(null=True)
    image = models.ImageField(blank=True, null=True, upload_to='requests', default='requests/request-default.jpg')
    offered_price = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.title

