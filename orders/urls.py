from django.urls import path
from .views import place_order, order_history

urlpatterns = [
    path('place-order/', place_order, name='place-order'),
    path('my-orders/', order_history, name='order-history'),
]
