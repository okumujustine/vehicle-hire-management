from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from customer.models import Customer


@login_required
def customer_list(request):
    customers = Customer.objects.all()
    context = {"customers": customers}
    return render(request, "customer/customer_list.html", context)
