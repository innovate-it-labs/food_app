from django.db import models
from users.models import SellerProfile
from django.utils import timezone
from django.contrib.auth import get_user_model
#from seller .models import Seller

User = get_user_model()

class Category(models.Model):
    Category_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    SubCategory_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.category.name})"

class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products',null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, blank=True)
    delivery_choices=[
        ("free", "Free Delivery"),
        ("paid", "Paid Delivery"),
    ]
    product_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    rating=models.DecimalField(max_digits=2, decimal_places=1)
    distance = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_charges = models.CharField(
    max_length=10,
    choices=delivery_choices,
    default="free"
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, blank=True)
    brand = models.CharField(max_length=100, blank=True, null=True)
    weight = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)  # optional
    tags = models.CharField(max_length=255, blank=True)  # comma-separated

    def __str__(self):
        return self.name
class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')
    alt_text = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.product.name}"