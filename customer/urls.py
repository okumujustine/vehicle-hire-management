from django.urls import path

from customer.views import customer_list, add_customer

app_name = "customer_app"

urlpatterns = [
    path("list", customer_list, name="customer_list_url"),
    path("add", add_customer, name="add_customer_url")
]
