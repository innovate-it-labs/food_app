from django.db import models
from users.models import CustomUser

class Seller(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='seller_profile')
    store_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.store_name
