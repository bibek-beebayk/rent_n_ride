from django.contrib import admin
from .models import Ad, VehicleMake, AdReview

admin.site.site_header = "RentN'Ride Admin"
admin.site.index_title = None
# Register your models here.
@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ['ad_title', 'owner', 'vehicle_type','vehicle_make', 'model', 'distance_travelled','asking_price', 'is_available', 'location']
    list_editable = []
    list_per_page = 20
    ordering = ['-created', 'ad_title']
    search_fields = ['ad_title__istartswith']
    list_filter = ['vehicle_type', 'created']

@admin.register(VehicleMake)
class VehicleMakeAdmin(admin.ModelAdmin):
    list_display = ['make']
    list_per_page = 20
    ordering = ['make']
    search_fields = ['make__istartswith']

@admin.register(AdReview)
class AdReviewAdmin(admin.ModelAdmin):
    list_display = ['ad', 'user', 'review_rating']
    list_per_page = 20
    ordering = ['ad', 'user']

