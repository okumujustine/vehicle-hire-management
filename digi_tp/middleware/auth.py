from django.shortcuts import redirect
from django.urls import reverse


class RedirectSuperUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_superuser and not request.path.startswith(reverse('admin:index')):
            return redirect(reverse('admin:index'))

        response = self.get_response(request)
        return response
