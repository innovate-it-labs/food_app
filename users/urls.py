from django.urls import path
from .views import SignupView, LoginView,ForgotPasswordView,ResetPasswordView,SellerRegisterView,SellerProfileView,CustomerRegisterView,CustomerProfileView,SetUserTypeView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('refresh-token/', TokenRefreshView.as_view(), name='refresh-token'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('reset-password/<uidb64>/<token>/', ResetPasswordView.as_view(), name='reset-password'),

    # Seller endpoints
    path('seller/register/', SellerRegisterView.as_view(), name='seller-register'),
    path('seller/profile/', SellerProfileView.as_view(), name='seller-profile'),
    
    #customer endpoints
    path('customer/register/', CustomerRegisterView.as_view(), name='user-register'),
    path('customer/profile/', CustomerProfileView.as_view(), name='user-profile'),

    path('set-user-type/',SetUserTypeView.as_view(),name="set-user-type")

    


]
