from django.urls import path

from vehicle.views import (
    delete_vehicle,
    add_vehicle,
    update_vehicle,
    VehicleListView
)

app_name = "vehicle_app"

urlpatterns = [
    path("list", VehicleListView.as_view(), name="vehicle_list_url"),
    path("add", add_vehicle, name="add_vehicle_url"),
    path("update/<vehicle_id>", update_vehicle, name="update_vehicle_url"),
    path("delete/<vehicle_id>", delete_vehicle, name="delete_vehicle_url")
]
