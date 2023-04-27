from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from customer.models import Customer
from customer.forms import CustomerForm


@login_required
def customer_list(request):
    customers = Customer.objects.all()
    context = {"customers": customers}
    return render(request, "customer/customer_list.html", context)


def add_customer(request):
    # perform vehicle creation
    if request.method == 'POST':
        form_to_save = CustomerForm(request.POST)
        if form_to_save.is_valid():
            form_to_save.save()
    context = {"add_customer_form": CustomerForm()}
    return render(request, "customer/add_customer.html", context)
