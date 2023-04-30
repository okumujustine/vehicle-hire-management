from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from user.models import CustomUser
from company.models import Company, CompanyUser


class CustomSignupForm(UserCreationForm):
    email = forms.EmailField(max_length=255, required=True)
    first_name = forms.CharField(max_length=255, required=True)
    last_name = forms.CharField(max_length=255, required=True)
    company_name = forms.CharField(max_length=200, required=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.is_active = True
        if commit:
            user.save()

        company_name = self.cleaned_data['company_name']
        existing_company = Company.objects.filter(name=company_name, companyuser__user=user).first()

        if existing_company:
            company = existing_company
        else:
            company = Company(name=company_name)
            company.save()

        company_user = CompanyUser(user=user, company=company)
        company_user.save()

        return user


class CustomLoginForm(forms.Form):
    email = forms.EmailField(
        max_length=255,
        label="Email",
        widget=forms.TextInput(attrs={"placeholder": "Email address", "required": "false"}),
        required=True
    )
    password = forms.CharField(
        max_length=255,
        label="Password",
        widget=forms.TextInput(attrs={"placeholder": "Password", "required": "false"}),
        required=True
    )
