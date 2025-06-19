from django.urls import path
from .views import cart_detail_view, add_to_cart_view, remove_from_cart_view

urlpatterns = [
    path('cart/', cart_detail_view, name='cart-detail'),
    path('cart/add/', add_to_cart_view, name='add-to-cart'),
    path('cart/remove/', remove_from_cart_view, name='remove-from-cart'),
]
