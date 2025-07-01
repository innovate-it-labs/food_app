from django.urls import path
from . import views 

urlpatterns = [
    path('products/', views.product_list, name='product-list'),
    path('products/<int:pk>/', views.product_detail, name='product-detail'),
    path('categories/', views.category_list, name='category-list'),
    path('subcategories/', views.subcategory_list, name='subcategory-list'),
    path('categories/create/', views.create_category, name='create-category'),
    path('categories/delete/<int:pk>/', views.delete_category, name='delete-category'),
    path('subcategory/create/', views.create_subcategory, name='create-subcategory'),
    path('subcategory/delete/<int:pk>/', views.delete_subcategory, name='delete-subcategory'),
    path('products/create/', views.create_product, name='create-product'),
    path('products/update/<int:pk>/', views.update_product, name='update-product'),
    path('products/delete/<int:pk>/', views.delete_product, name='delete-product'),
]
