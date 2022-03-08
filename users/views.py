from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .forms import ProfileForm
from requests.models import Request

# Create your views here.
def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist.')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Username or Password is incorrect.')

    return render(request, 'users/login.html')

def logoutUser(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User crested successfully.')

            login(request, user)
            return redirect('edit-account')

        else:
             messages.error(request, 'An error occured. Please try again later.')
           

    context = {'page' : page, 'form': form}
    return render(request, 'users/login.html', context)

def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)

def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile': profile}
    return render(request, 'users/user-profile.html', context)

@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    requests = profile.request_set.all()
    ads = profile.ad_set.all()
    context = {'profile': profile, 'requests': requests, 'ads': ads}
    return render(request, 'users/account.html', context)

@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('account')

    context = {'form': form}
    return render(request, 'users/profile-form.html', context)

@login_required(login_url='login')
def inbox(request):
    context={}
    return render(request, 'users/inbox.html', context)