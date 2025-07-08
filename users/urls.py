from django.urls import path
from .views import SignupView, LoginView,ForgotPasswordView,ResetPasswordView,SellerRegisterView,SellerProfileView,CustomerProfileView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('reset-password/<uidb64>/<token>/', ResetPasswordView.as_view(), name='reset-password'),

    # Seller endpoints
    path('seller/register/', SellerRegisterView.as_view(), name='seller-register'),
    path('seller/profile/', SellerProfileView.as_view(), name='seller-profile'),
    
    #customer endpoints
    path('customer/register/', CustomerProfileView.as_view(), name='user-profile'),
    path('customer/profile/', CustomerProfileView.as_view(), name='user-profile'),

    


]
