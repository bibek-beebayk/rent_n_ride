from asyncore import write
from contextlib import redirect_stderr
from urllib import response
from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import csv
from .forms import AdForm, AdReviewForm, AdSearchForm
from .models import Ad, AdReview
from requests.models import Request
from scripts.recommend import recommend_ads
import uuid

# Create your views here.

def ad(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    # print('SEARCH: ', search_query)

    ads = Ad.objects.filter(Q(ad_title__icontains=search_query) | Q(location__icontains=search_query))

    page = request.GET.get('page')
    results = 16
    paginator = Paginator(ads, results)

    try:
        ads = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        ads = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        ads = paginator.page(page)

    
    context = {'ads': ads, 'search_query': search_query, 'paginator': paginator}
    return render(request, 'ads/ads.html', context)

def ad_details(request, pk):
    count = 0
    sum = 0
    # average = None
    ad = Ad.objects.get(id=pk)  
    form = AdReviewForm()
    for review in ad.adreview_set.all():
        count+=1
        sum += int(review.review_rating)
    if count == 0:
        average = 0
    else:
        average = str(sum/count)[0:3]
    if request.method == "POST":
        form = AdReviewForm(request.POST)
        review = form.save(commit=False)
        review.ad = ad
        review.user = request.user.profile
        review.save()

        # update ad rating
        messages.success(request, 'Your review was submitted successfully.')
        return redirect('ad-details', pk=ad.id) 
    context = {'ad': ad, 'form': form, 'count':count, 'average':average }
    return render(request, 'ads/ad-details.html', context)

def nearbyAd(request):

    # remaining implementation

    return render(request, 'ads/nearby-ads.html')

def compareAds(request):
    # remaining implementation

    return render(request, 'ads/compare-ads.html')

@login_required(login_url='login')
def createAd(request):
    profile = request.user.profile
    form = AdForm()
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.owner = profile
            form.save()
            return redirect('user-ads')
    context = {'form': form}
    return render(request, 'ads/ad_form.html', context)
    

@login_required(login_url='login')
def updateAd(request, pk):
    profile = request.user.profile
    ad = profile.ad_set.get(id=pk)
    form = AdForm(instance=ad)
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES, instance=ad)
        if form.is_valid():
            form.save()
            return redirect('user-ads')
    context = {'form': form}
    return render(request, 'ads/ad_form.html', context)

@login_required(login_url='login')
def deleteAd(request, pk):
    profile = request.user.profile
    ad = profile.ad_set.get(id=pk)
    if request.method == 'POST':
        ad.delete()
        return redirect('user-ads')
    context = {'object': ad}
    return render(request, 'ads/delete_template.html', context)

@login_required(login_url='login')
def view_recommendations(request):
    user = request.user.profile
    aid = user.adreview_set.all().order_by('-review_rating')[0].ad_id
    adid = str(aid).replace('-', '')
    # print(usid)
    # user_id = usid.replace('-', '')
    # generate_csv()

    recommended_ads_list = recommend_ads(adid)
    recommended_uuid = []
    for item in recommended_ads_list:
        recommended_uuid.append(uuid.UUID(item))
    # ads = Ad.objects.all()
    recommended_ad_objects = []
    ads = Ad.objects.all()
    for item in recommended_uuid:
        for ad in ads:
            if (ad.id == item):
                recommended_ad_objects.append(ad)

    print(recommended_ad_objects)
    context = {'recommendations': recommended_ad_objects}

    return render(request, 'ads/recommendations.html', context)


def index(request):
    recent_ads = Ad.objects.all().order_by('-created')[:8]
    recent_requests = Request.objects.all().order_by('-created')[:8]
    context = {'recent_ads': recent_ads, 'recent_requests':recent_requests}
    return render(request, 'ads/index.html', context)

def advanced_search(request):
    form = AdSearchForm()
    context = {'form':form}
    return render(request, 'ads/advanced-search.html', context)


def export(request):
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['User', 'Ad', 'Rating'])
    for review in AdReview.objects.all().values_list('user', 'ad', 'review_rating'):
        writer.writerow(review)

    response['Content-Disposition'] = 'attachment; filename="ratings.csv"'

    return response