
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/', include('products.urls')),
    path('api/', include('carts.urls')),
    path('api/orders/', include('orders.urls')),
<<<<<<< HEAD

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
    #path('api/seller/',include('seller.urls')),
]
>>>>>>> ksaidurga
