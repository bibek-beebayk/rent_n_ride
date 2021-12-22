from django.db import models
import uuid

# Create your models here.


class Ad(models.Model):
    # ad_owner =
    # vehicle =
    ad_title = models.CharField(max_length=200, null=True)
    available_from = models.DateField(null=True)
    available_till = models.DateField(null=True)
    location = models.CharField(max_length=200, null=True)
    asking_price = models.DecimalField(
        max_digits=8, decimal_places=2, null=True)
    featured_image = models.ImageField(
        null=True, blank=True, upload_to='ads/', default='ads/ad-default.jpg')
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.ad_title
