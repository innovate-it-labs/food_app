# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from .models import CustomUser

# class CustomUserAdmin(BaseUserAdmin):
#     ordering = ['email']
#     list_display = ['email', 'full_name', 'is_active', 'is_staff', 'date_joined']
#     search_fields = ['email', 'full_name']
#     readonly_fields = ['date_joined']

#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Personal Info', {'fields': ('full_name',)}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
#         ('Important dates', {'fields': ('last_login', 'date_joined')}),
#     )

#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'full_name', 'password1', 'password2'),
#         }),
#     )

# admin.site.register(CustomUser, CustomUserAdmin)
