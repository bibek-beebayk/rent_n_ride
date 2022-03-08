from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import RequestForm

from requests.models import Request
# from .forms import AdForm
# from .models import Ad

# Create your views here.

def request(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    # print('SEARCH: ', search_query)

    requests = Request.objects.filter(Q(title__icontains=search_query) | Q(location__icontains=search_query))

    page = request.GET.get('page')
    results = 16
    paginator = Paginator(requests, results)

    try:
        requests = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        requests = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        requests = paginator.page(page)
   
    context = {'requests': requests, 'search_query': search_query, 'paginator': paginator}
    return render(request, 'requests/requests.html', context)

def request_details(request, pk):
    req = Request.objects.get(id=pk)
    context = {'request': req}
    return render(request, 'requests/request-details.html', context)

@login_required(login_url='login')
def createRequest(request):
    profile = request.user.profile
    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():
            req = form.save(commit=False)
            req.owner = profile
            form.save()
            return redirect('account')
    context = {'form': form}
    return render(request, 'requests/request_form.html', context)

@login_required(login_url='login')
def updateRequest(request, pk):
    profile = request.user.profile    
    req = profile.request_set.get(id=pk)
    form = RequestForm(instance=req)
    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES, instance=req)
        if form.is_valid():
            form.save()
            return redirect('account')
    context = {'form': form}
    return render(request, 'requests/request_form.html', context)

@login_required(login_url='login')
def deleteRequest(request, pk):
    profile = request.user.profile    
    req = profile.request_set.get(id=pk)
    if request.method == 'POST':
        req.delete()
        return redirect('account')
    context = {'object': req}
    return render(request, 'ads/delete_template.html', context)