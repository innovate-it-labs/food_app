from django.shortcuts import render

from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Category, SubCategory,ProductImage
from .serializers import ProductSerializer, CategorySerializer, SubCategorySerializer,ProductImageSerializer

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
<<<<<<< HEAD

=======

# to create acategory
@api_view(['POST'])
#@permission_classes([IsSellerUser])
def create_category(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#to delete a category
@api_view(['DELETE'])
#@permission_classes([IsSellerUser])
def delete_category(request, pk):
    try:
        category = Category.objects.get(pk=pk)
        category.delete()
        return Response({'message': 'Category deleted'}, status=status.HTTP_204_NO_CONTENT)
    except Category.DoesNotExist:
        return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

#to create a subcategory
@api_view(['POST'])
#@permission_classes([IsSellerUser])
def create_subcategory(request):
    serializer = SubCategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# to delete a subcategory
@api_view(['DELETE'])
#@permission_classes([IsSellerUser])
def delete_subcategory(request, pk):
    try:
        subcategory = SubCategory.objects.get(pk=pk)
        subcategory.delete()
        return Response({'message': 'SubCategory deleted'}, status=status.HTTP_204_NO_CONTENT)
    except SubCategory.DoesNotExist:
        return Response({'error': 'SubCategory not found'}, status=status.HTTP_404_NOT_FOUND)

# to add a product   
@api_view(['POST'])
#@permission_classes([IsSellerUser])
def create_product(request):
    seller = request.user.seller_profile
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(seller=seller)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#to delete a product
@api_view(['DELETE'])
#@permission_classes([IsSellerUser])
def delete_product(request, pk):
    try:
        product = Product.objects.get(pk=pk, seller__user=request.user)
        product.delete()
        return Response({'message': 'Product deleted'}, status=status.HTTP_204_NO_CONTENT)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
    
#to update a product
@api_view(['PUT', 'PATCH'])
#@permission_classes([IsSellerUser])
def update_product(request, pk):
    try:
        product = Product.objects.get(pk=pk, seller__user=request.user)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProductSerializer(product, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
>>>>>>> ksaidurga



