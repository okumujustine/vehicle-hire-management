from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from company.models import Company

from customer.models import Customer
from customer.forms import CustomerForm


@login_required
def customer_list(request):
    company_id = request.session.get('company_id')
    print("company_id", company_id)
    print("request_user", request.user)
    current_company_id = getattr(request, 'current_company_id', None)
    print("current_company_id", current_company_id)
    customers = Customer.objects.filter(company=company_id)
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
            company_id = request.session.get('company_id')
            if company_id:
                company = Company.objects.get(id=company_id)
                customer.company = company
            customer.save()

            messages.success(request, 'Customer created successfully.')

    context = {"add_customer_form": CustomerForm()}
    return render(request, "customer/add_customer.html", context)
