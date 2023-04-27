from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from vehicle.models import Vehicle
from vehicle.forms import VehicleForm


@login_required
def vehicle_list(request):
    all_vehicles = Vehicle.objects.all()

    context = {"vehicles": all_vehicles}
    return render(request, "vehicle/vehicle_list.html", context)


@login_required
def delete_vehicle(request, vehicle_id):
    vehicle_to_delete = Vehicle.objects.get(pk=vehicle_id)
    vehicle_to_delete.delete()
    return redirect("vehicle_app:vehicle_list_url")


def add_vehicle(request):
    # perform vehicle creation
    if request.method == 'POST':
        form_to_save = VehicleForm(request.POST)
        if form_to_save.is_valid():
            form_to_save.save()
    context = {"creat_vehicle_form": VehicleForm()}
    return render(request, "vehicle/add_vehicle.html", context)


def update_vehicle(request, vehicle_id):
    vehicle_to_update = Vehicle.objects.get(pk=vehicle_id)
    form = VehicleForm(request.POST or None, instance=vehicle_to_update)

    if form.is_valid():
        form.save()
        messages.success(request, "Vehicle successfully updated")

    context = {"vehicle": vehicle_to_update, "vehicle_form": form}
    return render(request, "vehicle/update_vehicle.html", context)
