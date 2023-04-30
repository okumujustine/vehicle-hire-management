from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Prefetch

from company.models import Company
from digi_tp.utils.session import check_session_and_user
from user.models import CustomUser


def company_auth_list(request):

    user = check_session_and_user(request)
    if not user:
        return redirect("user_app:user_login_url")

    companies = Company.objects.filter(companyuser__user=user).prefetch_related('companyuser_set')
    companies_and_roles = []
    for company in companies:
        company_user = company.companyuser_set.filter(user=user).first()
        user_role = company_user.role if company_user else None
        companies_and_roles.append({'company_name': company.name, 'user_role': user_role})

    context = {"companies_and_roles": companies_and_roles}
    return render(request, "company/company_auth_list.html", context)
