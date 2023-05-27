from django.urls import path

from order.views import OrderCreateView, OrderListView

app_name = "order_app"

urlpatterns = [
    path("list", OrderListView.as_view(), name="order_list_url"),
    path("create", OrderCreateView.as_view(), name="order_create_url"),
]
