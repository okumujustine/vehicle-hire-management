from django.urls import path

from order.views import order_list, OrderListView

app_name = "order_app"

urlpatterns = [
    path("list", OrderListView.as_view(), name="order_list_url"),
]
