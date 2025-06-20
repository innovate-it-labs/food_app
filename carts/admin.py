from django.contrib import admin
from .models import Cart, CartItem

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0  # Do not show extra empty forms
    readonly_fields = ['product', 'quantity']

class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'is_active')
    list_filter = ('is_active', 'created_at')
    search_fields = ('user__email',)
    readonly_fields = ('created_at',)
    inlines = [CartItemInline]

admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem)
