from django.utils import timezone
from django.contrib import messages
from user.models import CustomUser


def check_session(request):
    email = request.session.get('email')
    password = request.session.get('password')
    login_timestamp = request.session.get('login_timestamp')

    if not (email and password and login_timestamp):
        messages.error(request, "Session expired or invalid request")
        return None

    if (timezone.now().timestamp() - login_timestamp) > 1800:
        del request.session['email']
        del request.session['password']
        del request.session['login_timestamp']
        messages.error(request, "Session expired, login again")
        return None

    return {'email': email, 'password': password, 'login_timestamp': login_timestamp}


def check_session_and_user(request):
    if not check_session(request):
        return None

    email = request.session.get('email')
    password = request.session.get('password')

    try:
        user = CustomUser.objects.get(email=email)
    except CustomUser.DoesNotExist:
        messages.error(request, "User does not exist")
        return None

    if not user.check_password(password):
        messages.error(request, 'Invalid email or password')
        return None

    return user
