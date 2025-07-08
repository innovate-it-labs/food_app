
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from users.views import GoogleSocialLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/', include('products.urls')),
    path('api/', include('carts.urls')),
    path('api/orders/', include('orders.urls')),

    

    path('google-login/', GoogleSocialLoginView.as_view(), name='google-login'),
    
    path('accounts/', include('allauth.urls')),  # Required for OAuth flow


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
