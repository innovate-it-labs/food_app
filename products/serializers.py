from rest_framework import serializers
from . models import Category,SubCategory,Product,ProductImage
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['Category_id','name']
class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = SubCategory
        fields = ['Subcategory_id','name', 'category']
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['product_id', 'image', 'alt_text']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    subcategory = SubCategorySerializer(read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    class Meta:
        model=Product
        field='__all__'