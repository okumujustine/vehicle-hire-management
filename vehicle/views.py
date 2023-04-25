from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from vehicle.models import Vehicle
from vehicle.forms import VehicleForm


@login_required
def vehicle_list(request):
    all_vehicles = Vehicle.objects.all()

    # perform vehicle creation
    if request.method == 'POST':
        form_to_save = VehicleForm(request.POST)
        if form_to_save.is_valid():
            form_to_save.save()

    context = {"vehicles": all_vehicles, "creat_vehicle_form": VehicleForm()}
    return render(request, "vehicle/vehicle_list.html", context)
