
from django.urls import path
from .views import seller_dashboard  # Don't import from products here

urlpatterns = [
    path('dashboard/', seller_dashboard, name='seller-dashboard'),
]
