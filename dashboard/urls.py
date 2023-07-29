from django.urls import path
from dashboard.apis.simple_dashboard_views import  Dashboard

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard')
]