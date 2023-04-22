from django.contrib import admin
from django.urls import path

from dashboard.views import dashboard_home

urlpatterns = [
    path('', dashboard_home, name="dashboard_home"),
]
