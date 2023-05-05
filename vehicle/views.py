from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from company.models import Company

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
    if request.method == 'POST':
        number_plate = request.POST['number_plate']
        form = VehicleForm(request.POST)
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.created_by = request.user
            vehicle.updated_by = request.user
            company_id = request.session.get('company_id')
            if company_id:
                company = Company.objects.get(id=company_id)
                vehicle.company = company
            vehicle.save()
            messages.info(request, "Vehicle with number plate {} created successfully".format(number_plate))
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
