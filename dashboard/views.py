from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard_index(request):
    return render(request, "dashboard/dashboard_home.html")


@login_required
def dashboard_home(request):
    print("company_id", request.company_id)
    return render(request, "dashboard/dashboard_home.html")
