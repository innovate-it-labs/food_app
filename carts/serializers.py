from rest_framework import serializers
from .models import Cart, CartItem
from django.contrib.auth.models import User
from products.models import Product  # Assuming you have a Product model

class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'product_name', 'quantity', 'cart']
        read_only_fields = ['id', 'product_name']


class CartSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    cart_items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'user_name', 'created_at', 'is_active', 'cart_items']
        read_only_fields = ['id', 'created_at', 'user_name']
