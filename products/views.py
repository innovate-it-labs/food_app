from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Category, SubCategory
from .serializers import ProductSerializer, CategorySerializer, SubCategorySerializer

# to get product list
@api_view(['GET'])
def product_list(request):
    category = request.GET.get('category')
    subcategory = request.GET.get('subcategory')
    products = Product.objects.all()

    if category:
        products = products.filter(category__name__iexact=category)
    if subcategory:
        products = products.filter(subcategory__name__iexact=subcategory)

    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

# to get details of particular product
@api_view(['GET'])
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=404)

    serializer = ProductSerializer(product)
    return Response(serializer.data)

# to get category list
@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

# to get subcategory list
@api_view(['GET'])
def subcategory_list(request):
    subcategories = SubCategory.objects.all()
    serializer = SubCategorySerializer(subcategories, many=True)
    return Response(serializer.data)
