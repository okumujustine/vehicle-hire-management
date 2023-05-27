from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from order.models import Order
from order.resource import OrderResource


class OrderAdmin(ImportExportModelAdmin):
    resource_class = OrderResource


admin.site.register(Order, OrderAdmin)
