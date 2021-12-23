from django import forms
from django.shortcuts import render, redirect
from .forms import RequestForm

from requests.models import Request
# from .forms import AdForm
# from .models import Ad

# Create your views here.

def request(request):
    requests = Request.objects.all()
    context = {'requests': requests}
    return render(request, 'requests/requests.html', context)

def request_details(request, pk):
    req = Request.objects.get(id=pk)
    context = {'request': req}
    return render(request, 'requests/request-details.html', context)

def createRequest(request):
    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('requests-archive')
    context = {'form': form}
    return render(request, 'requests/request_form.html', context)

def updateRequest(request, pk):
    req = Request.objects.get(id=pk)
    form = RequestForm(instance=req)
    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES, instance=req)
        if form.is_valid():
            form.save()
            return redirect('requests-archive')
    context = {'form': form}
    return render(request, 'requests/request_form.html', context)

def deleteRequest(request, pk):
    req = Request.objects.get(id=pk)
    if request.method == 'POST':
        req.delete()
        return redirect('ads-archive')
    context = {'object': req}
    return render(request, 'ads/delete_template.html', context)