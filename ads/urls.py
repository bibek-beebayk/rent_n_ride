
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('ads/', views.ad, name='ads-archive'),
    path('ad/<str:pk>/', views.ad_details, name='ad-details'),
    path('create-ad/', views.createAd, name='create-ad'),
    path('update-ad/<str:pk>/', views.updateAd, name='update-ad'),
    path('delete-ad/<str:pk>/', views.deleteAd, name='delete-ad'),
    path('nearby-ads/', views.nearbyAd, name='nearby-ads'),
    path('compare-ads/', views.compareAds, name='compare-ads'),
    path('advanced-search/', views.advanced_search, name='advanced-search'),
    path('export/', views.export, name='export'),
    path('recommendations/', views.view_recommendations, name='recommendations'),

]
