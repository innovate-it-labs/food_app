from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser, CustomerProfile, SellerProfile
from django.utils.translation import gettext_lazy as _

# Inline for Customer Profile
class CustomerProfileInline(admin.StackedInline):
    model = CustomerProfile
    can_delete = False
    verbose_name_plural = 'Customer Profile'

# Inline for Seller Profile
class SellerProfileInline(admin.StackedInline):
    model = SellerProfile
    can_delete = False
    verbose_name_plural = 'Seller Profile'

# Custom User Admin
@admin.register(CustomUser)
class UserAdmin(BaseUserAdmin):
    inlines = []
    list_display = ('email', 'user_type', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('user_type', 'is_staff', 'is_superuser', 'is_active')
    search_fields = ('email', 'full_name')
    ordering = ('-date_joined',)
    readonly_fields = ('date_joined',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('full_name', 'user_type')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important Dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'user_type'),
        }),
    )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return []
        if obj.user_type == 'customer':
            return [CustomerProfileInline(self.model, self.admin_site)]
        elif obj.user_type == 'seller':
            return [SellerProfileInline(self.model, self.admin_site)]
        return []

# Register profiles separately as well (optional)
@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'city', 'state')
    search_fields = ('user__email', 'name', 'city')
    list_filter = ('city', 'state')

@admin.register(SellerProfile)
class SellerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'shop_name', 'gst_number', 'city', 'verified')
    search_fields = ('user__email', 'shop_name', 'gst_number')
    list_filter = ('city', 'verified')
