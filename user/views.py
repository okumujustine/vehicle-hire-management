from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from digi_tp.utils.message import MessageTypeExtraTags
from user.forms import CustomLoginForm, CustomSignupForm
from user.models import CustomUser


def not_authenticated(user):
    return not user.is_authenticated


@user_passes_test(not_authenticated, login_url='/dashboard/')
def login(request):
    if request.method == 'POST':
        login_form = CustomLoginForm(request.POST)
        if login_form.is_valid():
            email = request.POST['email']
            password = request.POST['password']

            try:
                user = CustomUser.objects.get(email=email)
            except CustomUser.DoesNotExist:
                messages.error(request, 'Invalid email or password')
            else:
                if not user.check_password(password):
                    messages.error(request, 'Invalid email or password')
                else:
                    request.session['email'] = email
                    request.session['password'] = password
                    request.session['login_timestamp'] = timezone.now().timestamp()
                    return redirect("company_app:company_auth_list_url")
    else:
        login_form = CustomLoginForm()

    return render(request, "account/login.html", context={"form": login_form})


@user_passes_test(not_authenticated, login_url='/dashboard/')
def signup(request):
    if request.method == "POST":
        signup_form = CustomSignupForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            messages.info(request,
                          "User account created successfully",
                          extra_tags=MessageTypeExtraTags.AUTH_MESSAGE.value
                          )

    else:
        signup_form = CustomSignupForm()

    return render(request, "account/signup.html", context={"form": signup_form})


@login_required
def logout_view(request):
    del request.session['company_id']
    logout(request)
    return redirect("user_app:user_login_url")
