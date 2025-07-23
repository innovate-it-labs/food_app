from django.shortcuts import render

from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Category, SubCategory,ProductImage
from .serializers import ProductSerializer, CategorySerializer, SubCategorySerializer,ProductImageSerializer
from users.permissions import IsSeller

# to get product list
@api_view(['GET'])
def products_by_subcategory(request, subcat_id):
    try:
        subcategory = SubCategory.objects.get(SubCategory_id=subcat_id)
    except SubCategory.DoesNotExist:
        return Response({'error': 'SubCategory not found'}, status=status.HTTP_404_NOT_FOUND)

    products = Product.objects.filter(subcategory=subcategory)
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

# to get subcategory list of a particular category
@api_view(['GET'])
def subcategories_by_category(request, category_id):
    try:
        category = Category.objects.get(Category_id=category_id)
    except Category.DoesNotExist:
        return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

    subcategories = category.subcategories.all()
    serializer = SubCategorySerializer(subcategories, many=True)
    return Response(serializer.data)



@api_view(['POST'])
#@permission_classes([IsSeller])
def create_category(request):
    permission_classes = [IsSeller]
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#to delete a category
@api_view(['DELETE'])
#@permission_classes([IsSeller])
def delete_category(request, pk):
    #permission_classes = [IsSeller]
    try:
        category = Category.objects.get(pk=pk)
        category.delete()
        return Response({'message': 'Category deleted'}, status=status.HTTP_204_NO_CONTENT)
    except Category.DoesNotExist:
        return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

#to create a subcategory
@api_view(['POST'])
#@permission_classes([IsSeller])
def create_subcategory(request):
    #permission_classes = [IsSeller]
    serializer = SubCategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# to delete a subcategory
@api_view(['DELETE'])
#@permission_classes([IsSeller])
def delete_subcategory(request, pk):
    #permission_classes = [IsSeller]
    try:
        subcategory = SubCategory.objects.get(pk=pk)
        subcategory.delete()
        return Response({'message': 'SubCategory deleted'}, status=status.HTTP_204_NO_CONTENT)
    except SubCategory.DoesNotExist:
        return Response({'error': 'SubCategory not found'}, status=status.HTTP_404_NOT_FOUND)

# to add a product   
@api_view(['POST'])
#@permission_classes([IsSeller])
def create_product(request):
    #permission_classes = [IsSeller]
    seller = request.user.seller_profile
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(seller=seller)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#to delete a product
@api_view(['DELETE'])
#@permission_classes([IsSeller])
def delete_product(request, pk):
    #permission_classes = [IsSeller] 
    try:
        product = Product.objects.get(pk=pk, seller__user=request.user)
        product.delete()
        return Response({'message': 'Product deleted'}, status=status.HTTP_204_NO_CONTENT)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
    
#to update a product
@api_view(['PUT', 'PATCH'])
#@permission_classes([IsSeller])
def update_product(request, pk):
    #permission_classes = [IsSeller] 
    try:
        product = Product.objects.get(pk=pk, seller__user=request.user)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProductSerializer(product, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



