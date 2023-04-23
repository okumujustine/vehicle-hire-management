from django.contrib import admin
from django.urls import path

from dashboard.views import dashboard_home


app_name = 'dashboard_app'

urlpatterns = [
    path('', dashboard_home, name="dashboard_home_url"),
]
