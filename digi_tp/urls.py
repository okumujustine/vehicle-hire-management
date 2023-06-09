from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from dashboard.views import dashboard_index

urlpatterns = [
    path("", dashboard_index, name="dashboard_index_url"),
    path("admin/", admin.site.urls),
    path("user/", include("user.urls", namespace="user_app")),
    path("dashboard/", include("dashboard.urls", namespace="dashboard_app")),
    path("customer/", include("customer.urls", namespace="customer_app")),
    path("vehicle/", include("vehicle.urls", namespace="vehicle_app")),
    path("order/", include("order.urls", namespace="order_app")),
    path("company/", include("company.urls", namespace="company_app")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
