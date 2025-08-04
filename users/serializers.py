from rest_framework import serializers
from .models import CustomUser, CustomerProfile, SellerProfile
import re
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers


class SetUserTypeSerializer(serializers.Serializer):
    user_type = serializers.ChoiceField(choices=[('seller', 'Seller'), ('customer', 'Customer')])
    def save(self, **kwargs):
        user = self.context['request'].user
        user.user_type = self.validated_data['user_type']
        user.save()

        return user


class UserSignupSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user




class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True, min_length=6)


class CustomerProfileSerializer(serializers.ModelSerializer):
    date_of_birth = serializers.DateField(
        format="%d/%m/%Y",                     # Output format
        input_formats=["%d/%m/%Y"],            # Accepted input format
        required=False,                         # ✅ Add this line
        allow_null=True                          # ✅ And this
    )
    class Meta:
        model = CustomerProfile
        fields = ['name','house_number', 'address', 'city', 'gender','date_of_birth','phone_number','profile_picture']



    def validate_name(self, value):
        if not re.match(r'^[A-Za-z0-9 ]+$', value):
            raise serializers.ValidationError("Name should only contain letters,number and spaces.")
        return value

    def validate_city(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("City name too short.")
        return value
    


class SellerProfileSerializer(serializers.ModelSerializer):
    date_of_birth = serializers.DateField(
        format="%d/%m/%Y",                     # Output format
        input_formats=["%d/%m/%Y"]             # Accepted input format
    )
    class Meta:
        model = SellerProfile
        fields = ['name','phone_number','date_of_birth','profile_picture']
        read_only_fields = ['verified']

    

    def validate_shop_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Shop name must be at least 3 characters.")
        return value
