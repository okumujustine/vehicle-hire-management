from django.shortcuts import render

from user.forms import CustomLoginForm, CustomSignupForm


def login(request):
    login_form = CustomLoginForm()
    return render(request, "account/login.html", context={"form": login_form})


def siginup(request):
    signup_form = CustomSignupForm()
    return render(request, "account/siginup.html", context={"form": signup_form})
