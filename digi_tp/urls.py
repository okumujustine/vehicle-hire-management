from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("dashboard/", include("dashboard.urls", namespace="dashboard_app")),
    path("customer/", include("customer.urls", namespace="customer_app")),
]
