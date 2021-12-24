from django import forms
from django.shortcuts import render, redirect
from .forms import AdForm
from .models import Ad
from requests.models import Request

# Create your views here.

def ad(request):
    ads = Ad.objects.all()
    context = {'ads': ads}
    return render(request, 'ads/ads.html', context)

def ad_details(request, pk):
    ad = Ad.objects.get(id=pk)
    context = {'ad': ad}
    return render(request, 'ads/ad-details.html', context)

def createAd(request):
    form = AdForm()
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ads-archive')
    context = {'form': form}
    return render(request, 'ads/ad_form.html', context)

def updateAd(request, pk):
    ad = Ad.objects.get(id=pk)
    form = AdForm(instance=ad)
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES, instance=ad)
        if form.is_valid():
            form.save()
            return redirect('ads-archive')
    context = {'form': form}
    return render(request, 'ads/ad_form.html', context)

def deleteAd(request, pk):
    ad = Ad.objects.get(id=pk)
    if request.method == 'POST':
        ad.delete()
        return redirect('ads-archive')
    context = {'object': ad}
    return render(request, 'ads/delete_template.html', context)

def index(request):
    recent_ads = Ad.objects.all().order_by('-created')[:8]
    recent_requests = Request.objects.all().order_by('-created')[:8]
    context = {'recent_ads': recent_ads, 'recent_requests':recent_requests}
    return render(request, 'ads/index.html', context)