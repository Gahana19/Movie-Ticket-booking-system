from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser, PasswordResetRequest

@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    list_display = (
         'email', 'first_name', 'last_name',
         'role', 'is_active', 'is_staff', 'date_joined')
    list_filter = ('role', 'is_active', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('-date_joined',)
    fieldsets = (
            (None, {'fields': ('email', 'password')}),
            ('Personal Info', {'fields': ('first_name',  'last_name')}),
            ('Permissions', {
            'fields': (
                'role', 'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                ),
            }),
            ('Important Dates', {'fields': ('last_login', 'date_joined')}),
            )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
            'email', 'first_name', 'last_name',
            'password1', 'password2', 'role'
            ),
            }),
)
@admin.register(PasswordResetRequest)
class PasswordResetRequestAdmin(admin.ModelAdmin):
    list_display = ('email', 'user', 'created_at', 'is_valid')
    list_filter = ('created_at',)
    search_fields = ('email', 'user__email')
    readonly_fields = ('token', 'created_at')
def is_valid(self, obj):
    return obj.is_valid()
is_valid.boolean = True