from django.urls import path

from customer.views import customer_list

app_name = "customer_app"

urlpatterns = [
    path("list", customer_list, name="customer_list_url"),
]
