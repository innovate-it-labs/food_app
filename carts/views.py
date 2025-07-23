from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Cart, CartItem
from products.models import Product
from .serializers import CartSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


@api_view(['GET'])

def cart_detail_view(request):
    user = request.user  
    cart, _ = Cart.objects.get_or_create(user=user, is_active=True)
    serializer = CartSerializer(cart)
    return JsonResponse(serializer.data, status=200, safe=False)


@api_view(['POST'])
def add_to_cart_view(request):
    user = request.user
    product_id = request.data.get('product_id')
    quantity = int(request.data.get('quantity', 1))

    if not product_id:
        return JsonResponse({'error': 'Product ID required'}, status=400)

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)

    cart, _ = Cart.objects.get_or_create(user=user, is_active=True)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += quantity
    else:
        cart_item.quantity = quantity
    cart_item.save()

    return JsonResponse({'message': 'Product added to cart'}, status=200)


@api_view(['POST'])
def remove_from_cart_view(request):
    user = request.user
    product_id = request.data.get('product_id')
    quantity = int(request.data.get('quantity', 1))

    if not product_id:
        return JsonResponse({'error': 'Product ID required'}, status=400)

    try:
        cart = Cart.objects.get(user=user, is_active=True)
        cart_item = CartItem.objects.get(cart=cart, product_id=product_id)
    except (Cart.DoesNotExist, CartItem.DoesNotExist):
        return JsonResponse({'error': 'Item not found in cart'}, status=404)

    if cart_item.quantity > quantity:
        cart_item.quantity -= quantity
        cart_item.save()
    else:
        cart_item.delete()

    return JsonResponse({'message': 'Product removed from cart'}, status=200)
