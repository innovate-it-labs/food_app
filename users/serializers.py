

from rest_framework import serializers
from .models import CustomUser, UserProfile, SellerModel


class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'full_name', 'password', 'user_type']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user



class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True, min_length=6)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['name', 'address', 'city', 'state', 'preferences', 'profile_picture']



class SellerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerModel
        fields = ['shop_name', 'gst_number', 'address', 'logo', 'verified']
        read_only_fields = ['verified']  

