from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, ContactMessage


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """إدارة نموذج المستخدم في لوحة التحكم"""
    list_display = ('username', 'email', 'user_type', 'is_active', 'is_staff', 'date_joined')
    list_filter = ('user_type', 'is_active', 'is_staff')
    search_fields = ('username', 'email', 'phone')
    ordering = ('-date_joined',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('المعلومات الشخصية', {'fields': ('first_name', 'last_name', 'email', 'phone', 'address')}),
        ('الصلاحيات', {'fields': ('user_type', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('التواريخ', {'fields': ('last_login', 'date_joined')}),
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """إدارة رسائل التواصل"""
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('created_at',)
