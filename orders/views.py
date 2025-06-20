from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Order, OrderItem
from .serializers import OrderSerializer
from carts.models import Cart, CartItem
from django.contrib.auth import get_user_model

User = get_user_model()

def get_dummy_user():
    return User.objects.first()

@api_view(['POST'])
def place_order(request):
    user = get_dummy_user()

    try:
        cart = Cart.objects.get(user=user, is_active=True)
    except Cart.DoesNotExist:
        return Response({'error': 'Cart is empty'}, status=status.HTTP_400_BAD_REQUEST)

    cart_items = CartItem.objects.filter(cart=cart)
    if not cart_items.exists():
        return Response({'error': 'Cart is empty'}, status=status.HTTP_400_BAD_REQUEST)

    total_amount = sum(item.product.price * item.quantity for item in cart_items)

    order = Order.objects.create(user=user, total_amount=total_amount)

    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
        )

    # Empty the cart after placing order
    cart_items.delete()
    cart.is_active = False
    cart.save()

    serializer = OrderSerializer(order)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def order_history(request):
    user = get_dummy_user()
    orders = Order.objects.filter(user=user).order_by('-created_at')
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data, status=200)
