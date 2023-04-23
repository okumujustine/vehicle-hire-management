from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def customer_list(request):
    return render(request, "customer/customer_list.html")
