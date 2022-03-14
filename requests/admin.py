from django.contrib import admin
from .models import Request

# Register your models here.

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'vehicle_type', 'location', 'offered_price', 'created']
    list_per_page = 20
    list_filter = ['vehicle_type', 'created']
    search_fields = ['title__istartswith']
    list_editable = ['offered_price']