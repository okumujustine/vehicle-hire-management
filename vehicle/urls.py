from django.urls import path

from vehicle.views import vehicle_list

app_name = "vehicle_app"

urlpatterns = [
    path("list", vehicle_list, name="vehicle_list_url"),
]
