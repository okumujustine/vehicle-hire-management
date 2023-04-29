from django.contrib import admin
from django.urls import path, include

from dashboard.views import dashboard_index

urlpatterns = [
    path("", dashboard_index, name="dashboard_index_url"),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("dashboard/", include("dashboard.urls", namespace="dashboard_app")),
    path("customer/", include("customer.urls", namespace="customer_app")),
    path("vehicle/", include("vehicle.urls", namespace="vehicle_app")),
    path("order/", include("order.urls", namespace="order_app")),
]
