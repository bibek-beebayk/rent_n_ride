from django.urls import path
from . import views


urlpatterns = [
    path('', views.request, name='requests-archive'),
    path('request/<str:pk>/', views.request_details, name='request-details'),
    path('create-request/', views.createRequest, name='create-request'),
    path('update-request/<str:pk>/', views.updateRequest, name='update-request'),
    path('delete-request/<str:pk>/', views.deleteRequest, name='delete-request'),

]