from django.urls import path
from . import views


urlpatterns = [
    path('requests/', views.request, name='requests-archive'),
    # path('ad/<str:pk>/', views.ad_details, name='ad-details'),
    # path('create-ad/', views.createAd, name='create-ad'),
    # path('update-ad/<str:pk>/', views.updateAd, name='update-ad'),
    # path('delete-ad/<str:pk>/', views.deleteAd, name='delete-ad'),

]