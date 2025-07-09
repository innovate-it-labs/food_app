from django.contrib import admin
from .models import Seller

@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('store_name', 'user', 'phone')
    search_fields = ('store_name', 'user__email', 'user__full_name', 'phone')
    list_filter = ('store_name',)
