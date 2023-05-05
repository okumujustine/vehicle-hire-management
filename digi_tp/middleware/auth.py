from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages


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
        if request.user.is_authenticated and not company_id and not request.path.startswith(reverse('admin:index')):
            messages.warning(request, 'Please select a company to access this page')
            return redirect(reverse('user_app:user_login_url'))

        request.company_id = company_id
        response = self.get_response(request)
        return response
