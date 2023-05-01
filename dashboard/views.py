from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard_index(request):
    return render(request, "dashboard/dashboard_home.html")


@login_required
def dashboard_home(request):
    company_id = request.session.get('company_id')
    print("company_id", company_id)
    return render(request, "dashboard/dashboard_home.html")
