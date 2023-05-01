from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.db.models import Q


class EmailAuthentication(BaseBackend):
    def get_user(self, user_id: int):
        try:
            return get_user_model().objects.get(pk=user_id)
        except get_user_model().DoesNotExist:
            return None

    def authenticate(self, request, username=None, password=None, company_id=None):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(Q(email__iexact=username))
            if user.check_password(password):
                request.session['company_id'] = company_id
                request.current_company_id = company_id
                return user
        except UserModel.DoesNotExist:
            return None
