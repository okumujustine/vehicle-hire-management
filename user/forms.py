from django import forms
from django.contrib.auth.forms import UserCreationForm


class CustomSignupForm():
    first_name = forms.CharField(
        max_length=255,
        label="First Name",
        widget=forms.TextInput(attrs={"placeholder": "First name"}),
    )
    last_name = forms.CharField(
        max_length=255,
        label="Last Name",
        widget=forms.TextInput(attrs={"placeholder": "Last name"}),
    )

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if not first_name:
            raise forms.ValidationError("First name is required.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")
        if not last_name:
            raise forms.ValidationError("Last name is required.")
        return last_name

    def save(self, request):
        print("save user")


class CustomLoginForm(forms.Form):
    email = forms.EmailField(
        max_length=255,
        label="Email",
        widget=forms.TextInput(attrs={"placeholder": "Email address", "required": "false"}),
    )
    password = forms.CharField(
        max_length=255,
        label="Password",
        widget=forms.TextInput(attrs={"placeholder": "Password", "required": "false"}),
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email:
            raise forms.ValidationError("Email is required.")
        return email

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if not password:
            raise forms.ValidationError("Password is required.")
        return password

    def save(self, request):
        print("login user")