from rest_framework import generics, status, serializers, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str

import requests


from .models import SellerProfile, CustomerProfile 
from .serializers import (
    UserSignupSerializer,
    ForgotPasswordSerializer,
    ResetPasswordSerializer,
    SellerProfileSerializer,
    CustomerProfileSerializer,
    SetUserTypeSerializer
)


User = get_user_model()



class SetUserTypeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = SetUserTypeSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "User type created successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class GoogleSocialLoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        access_token = request.data.get('access_token')

        if not access_token:
            return Response({'error': 'Access token required.'}, status=400)

        # Verify token and get user info from Google
        google_userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
        response = requests.get(
            google_userinfo_url,
            params={'access_token': access_token}
        )

        if response.status_code != 200:
            return Response({'error': 'Invalid Google token'}, status=400)

        user_data = response.json()
        email = user_data.get('email')
        name = user_data.get('name')

        if not email:
            return Response({'error': 'Google token did not return email'}, status=400)

       
        user, created = User.objects.get_or_create(email=email)
        if created:
            user.set_unusable_password()  # So no login via password
            user.save()

        
        refresh = RefreshToken.for_user(user)
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'user': {
                'email': user.email,
                'name': name,
                'id': user.id
            }
        })



class SignupView(generics.CreateAPIView):
    serializer_class = UserSignupSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        self.user = authenticate(
            request=self.context.get('request'),
            email=attrs.get("email"),
            password=attrs.get("password")
        )
        if self.user is None:
            raise serializers.ValidationError("Invalid credentials")

        refresh = self.get_token(self.user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token), 
            'email': self.user.email,
        }

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token


class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    permission_classes = [permissions.AllowAny]


class ForgotPasswordView(generics.GenericAPIView):
    serializer_class = ForgotPasswordSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({'message': 'If this email exists, a reset link has been sent.'}, status=status.HTTP_200_OK)

            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)

            reset_link = f"https://your-frontend-domain.com/reset-password/{uid}/{token}/"  

            subject = "Password Reset Request - Foodie App"
            text_message = f"Click the link to reset your password: {reset_link}"
            html_message = f"""
                <p>Hi {user.email},</p>
                <p>We received a request to reset your password.</p>
                <p><a href="{reset_link}"> reset your password</a></p>
                <p>If you didn't request this, please ignore this email.</p>
                <p>Thanks,<br>Foodie Team</p>
            """

            email_message = EmailMultiAlternatives(
                subject=subject,
                body=text_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[user.email],
            )
            email_message.attach_alternative(html_message, "text/html")
            email_message.send()

            return Response({'message': 'Reset link sent successfully.'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordView(generics.GenericAPIView):
    serializer_class = ResetPasswordSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, uidb64, token):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            try:
                uid = force_str(urlsafe_base64_decode(uidb64))
                user = User.objects.get(pk=uid)
            except (TypeError, ValueError, OverflowError, User.DoesNotExist):
                return Response({'error': 'Invalid reset link.'}, status=status.HTTP_400_BAD_REQUEST)

            if not default_token_generator.check_token(user, token):
                return Response({'error': 'Token is invalid or has expired.'}, status=status.HTTP_400_BAD_REQUEST)

            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response({'message': 'Password reset successfully.'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



class SellerProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = SellerProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return SellerProfile.objects.get(user=self.request.user)

class SellerRegisterView(generics.CreateAPIView):
    serializer_class = SellerProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if SellerProfile.objects.filter(user=self.request.user).exists():
            raise serializers.ValidationError("Seller profile already exists.")
        serializer.save(user=self.request.user)





class CustomerProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = CustomerProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return get_object_or_404(CustomerProfile, user=self.request.user)
    
class CustomerRegisterView(generics.CreateAPIView):
    serializer_class=CustomerProfileSerializer
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if  CustomerProfile.objects.filter(user=self.request.user).exists():
            raise serializers.ValidationError("Customer profile already exists.")
        serializer.save(user=self.request.user)

