from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = ('category', 'name')

    def __str__(self):
        return f"{self.category.name} - {self.name}"

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, blank=True)
    delivery_choices=[
        ("free", "Free Delivery"),
        ("paid", "Paid Delivery"),
    ]
    id = models.BigAutoField(primary_key=True)
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
    image1 = models.ImageField(upload_to='product_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='product_images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='product_images/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, blank=True)
    brand = models.CharField(max_length=100, blank=True, null=True)
    weight = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)  # optional
    tags = models.CharField(max_length=255, blank=True)  # comma-separated

    def __str__(self):
        return self.name
