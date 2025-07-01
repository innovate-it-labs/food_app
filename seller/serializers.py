
from rest_framework import serializers
from .models import Seller
from users.serializers import CustomUserSerializer

class SellerSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Seller
        fields = ['user', 'store_name', 'phone', 'address']
