from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages

from company.models import Company


class RedirectSuperUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_superuser and not request.path.startswith(reverse('admin:index')):
            return redirect(reverse('admin:index'))

        response = self.get_response(request)
        return response


class CompanyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        company_id = request.session.get('company_id')
        if not request.path.startswith(reverse('admin:index')):
            if request.user.is_authenticated and not company_id:
                messages.warning(request, 'Session expired, login again')
                return redirect(reverse('user_app:user_login_url'))

            if request.user.is_authenticated:
                request.company_id = company_id
                current_company = get_object_or_404(Company, id=company_id)
                request.current_company = current_company

        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        if not request.path.startswith(reverse('admin:index')):
            response.context_data['current_company'] = request.current_company
        return response
