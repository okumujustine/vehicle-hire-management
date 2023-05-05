from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from company.models import Company

from customer.models import Customer
from customer.forms import CustomerForm


@login_required
def customer_list(request):
    customers = Customer.objects.filter(company=request.company_id)
    context = {"customers": customers}
    return render(request, "customer/customer_list.html", context)


def add_customer(request):
    # perform vehicle creation
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.created_by = request.user
            customer.updated_by = request.user

            company = Company.objects.get(id=request.company_id)
            customer.company = company

            customer.save()

            messages.success(request, 'Customer created successfully.')

    context = {"add_customer_form": CustomerForm()}
    return render(request, "customer/add_customer.html", context)
