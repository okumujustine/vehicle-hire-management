from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from vehicle.models import Vehicle


@login_required
def vehicle_list(request):
    all_vehicles = Vehicle.objects.all()
    context = {"vehicles": all_vehicles}
    return render(request, "vehicle/vehicle_list.html", context)
