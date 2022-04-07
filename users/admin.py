from django.contrib import admin
from .models import Profile, Message, UserReview

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'name', 'gender', 'email', 'phone', 'created']
    list_per_page = 20
    search_fields = ['name__istartswith']
    list_filter = ['created', 'gender']

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['sender', 'receiver', 'subject', 'created']
    liat_per_page = 20
    list_filter = ['created']
    search_fields = ['sender__istartswith', 'receiver__istartswith', 'subject']
@admin.register(UserReview)
class UserReviewAdmin(admin.ModelAdmin):
    pass
