from django.shortcuts import render, redirect
from django.contrib import messages

from company.models import Company
from digi_tp.utils.session import check_session, check_session_and_user
from django.contrib.auth import authenticate, login


def company_auth_list(request):

    if request.method == 'POST':
        current_auth_session = check_session(request)
        if not check_session(request):
            messages.error(request, "Invalid or expired session, login again")
            return redirect("user_app:user_login_url")

        selected_company_id = request.POST.get('company')
        if not selected_company_id:
            messages.error(request, "A company must be selected")

        user = authenticate(
            request=request,
            username=current_auth_session["email"],
            password=current_auth_session["password"],
            company_id=selected_company_id
        )
        if user is not None:
            login(request, user)
            return redirect("dashboard_app:dashboard_home_url")
        else:
            messages.error(request, "Invalid email or password")
            return redirect("user_app:user_login_url")

    user = check_session_and_user(request)
    if not user:
        messages.error(request, "Invalid or expired session, login again")
        return redirect("user_app:user_login_url")

    companies = Company.objects.filter(companyuser__user=user).prefetch_related('companyuser_set')
    companies_and_roles = []
    for company in companies:
        company_user = company.companyuser_set.filter(user=user).first()
        user_role = company_user.role if company_user else None
        companies_and_roles.append({'company_id': company.pk, 'company_name': company.name, 'user_role': user_role})

    context = {"companies_and_roles": companies_and_roles}
    return render(request, "company/company_auth_list.html", context)
