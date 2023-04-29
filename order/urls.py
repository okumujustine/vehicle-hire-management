from django.urls import path

from order.views import order_list

app_name = "order_app"

urlpatterns = [
    path("list", order_list, name="order_list_url"),
]
