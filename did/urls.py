"""
URL configuration for did project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # لوحة الإدارة
    path('admin/', admin.site.urls),

    # التطبيق الأساسي (المستخدمين، الصفحات العامة)
    path('', include('core.urls')),  

    # تطبيق المتجر (المنتجات، التصنيفات)
    path('store/', include('store.urls')),

    # تطبيق الطلبات والمدفوعات
    path('orders/', include('orders.urls')),
]

# إعدادات ملفات static و media أثناء التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
