from django.urls import path
from . import views


urlpatterns = [
    path('', views.vehicles, name='vehicles-archive'),
    path('vehicle/<str:pk>/', views.vehicle_details, name='vehicle-details'),
    path('create-vehicle/', views.createVehicle, name='create-vehicle'),
    path('update-vehicle/<str:pk>/', views.updateVehicle, name='update-vehicle'),
    path('delete-vehicle/<str:pk>/', views.deleteVehicle, name='delete-vehicle'),

]