from django.shortcuts import render
# seller/views.py

# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.response import Response
# from rest_framework import status
# from orders.models import Order
# from products.models import Product
# from products.serializers import ProductSerializer
# from orders.serializers import OrderSerializer 
# #from products.permissions import IsSellerUser

# @api_view(['GET'])
# #@permission_classes([IsSellerUser])
# def seller_dashboard(request):
#     from orders.models import Order
#     from products.models import Product
#     from orders.serializers import OrderSerializer

#     seller = request.user.seller_profile

#     products = Product.objects.filter(seller=seller)
#     product_ids = products.values_list('id', flat=True)

#     orders = Order.objects.filter(product_id__in=product_ids)

#     total_orders = orders.count()
#     total_revenue = sum(order.total_price for order in orders)

#     data = {
#         'total_products': products.count(),
#         'total_orders': total_orders,
#         'total_revenue': float(total_revenue),
#     }

#     return Response(data)


