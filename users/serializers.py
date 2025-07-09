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


# class UserSignupSerializer(RegisterSerializer):
#     username = None  # remove the username field
#     email = serializers.EmailField(required=True)

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields.pop('username', None)

#     def get_cleaned_data(self):
#         data_dict = super().get_cleaned_data()
#         data_dict.pop('username', None)  # ensure username is not used
#         return data_dict




class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True, min_length=6)


class CustomerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerProfile
        fields = ['name', 'address', 'city', 'state', 'preferences', 'profile_picture']

    def validate_name(self, value):
        if not re.match(r'^[A-Za-z ]+$', value):
            raise serializers.ValidationError("Name should only contain letters and spaces.")
        return value

    def validate_city(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("City name too short.")
        return value
    


class SellerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerProfile
        fields = ['shop_name', 'gst_number', 'address', 'logo', 'verified']
        read_only_fields = ['verified']

    

    def validate_shop_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Shop name must be at least 3 characters.")
        return value
