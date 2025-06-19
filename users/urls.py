from django.urls import path
<<<<<<< HEAD
from .views import SignupView, LoginView
from rest_framework_simplejwt.views import TokenRefreshView
 
=======
from .views import SignupView, LoginView,ForgotPasswordView,ResetPasswordView
from rest_framework_simplejwt.views import TokenRefreshView


>>>>>>> 563a36169d6fe5cce01fb8e922f0b34ef5863817
urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
<<<<<<< HEAD
=======
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('reset-password/<uidb64>/<token>/', ResetPasswordView.as_view(), name='reset-password'),

>>>>>>> 563a36169d6fe5cce01fb8e922f0b34ef5863817
]
 