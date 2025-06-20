from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['product', 'quantity', 'price']

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'total_amount', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__email',)
    readonly_fields = ('created_at',)
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
