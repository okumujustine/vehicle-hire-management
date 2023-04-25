from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def vehicle_list(request):
    return render(request, "vehicle/vehicle_list.html")
