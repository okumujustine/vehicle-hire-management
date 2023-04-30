from django.urls import path

from company.views import company_auth_list

app_name = "company_app"

urlpatterns = [
    path("company_auth_list", company_auth_list, name="company_auth_list_url"),
]
