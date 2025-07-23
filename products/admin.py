from django.contrib import admin
from .models import Category, SubCategory, Product, ProductImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['Category_id', 'name']
    search_fields = ['name']


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['SubCategory_id', 'name', 'category']
    list_filter = ['category']
    search_fields = ['name']


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'name', 'price', 'seller', 'category', 'is_active', 'created_at']
    list_filter = ['is_active', 'category', 'subcategory']
    search_fields = ['name', 'tags', 'seller__user__email']
    inlines = [ProductImageInline]
    autocomplete_fields = ['category', 'subcategory', 'seller']


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'alt_text']



# from django.contrib import admin
# from .models import Category, SubCategory, Product,ProductImage

# admin.site.register(Category)
# admin.site.register(SubCategory)
# class ProductImageInline(admin.TabularInline):
#     model = ProductImage
#     extra = 1 
# class ProductAdmin(admin.ModelAdmin):
#     inlines = [ProductImageInline]
# admin.site.register(Product,ProductAdmin)

