from rest_framework import serializers
from . models import Category,SubCategory,Product
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']
class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = SubCategory
        fields = ['name', 'category']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    subcategory = SubCategorySerializer(read_only=True)
    class Meta:
        model=Product
        field='__all__'