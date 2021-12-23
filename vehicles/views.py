from django.shortcuts import render, redirect
from vehicles.forms import VehicleForm

from vehicles.models import Vehicle

# Create your views here.

def vehicles(request):
    vehicles = Vehicle.objects.all()
    context = {'vehicles': vehicles}
    return render(request, 'vehicles/vehicles.html', context)

def vehicle_details(request, pk):
    vehicle = Vehicle.objects.get(id=pk)
    context = {'vehicle': vehicle}
    return render(request, 'vehicles/vehicle-details.html', context)

def createVehicle(request):
    form = VehicleForm()
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('vehicles-archive')
    context = {'form': form}
    return render(request, 'vehicles/vehicle-form.html', context)

def updateVehicle(request, pk):
    vehicle = Vehicle.objects.get(id=pk)
    form = VehicleForm(instance=vehicle)
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('vehicles-archive')
    context = {'form': form}
    return render(request, 'vehicles/vehicle-form.html', context)

def deleteVehicle(request, pk):
    vehicle = Vehicle.objects.get(id=pk)
    if request.method == 'POST':
        vehicle.delete()
        return redirect('vehicles-archive')
    context = {'object': vehicle}
    return render(request, 'ads/delete_template.html', context)
