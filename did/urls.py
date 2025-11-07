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
    # 🧭 لوحة الإدارة
    path('admin/', admin.site.urls),

    # 🧩 التطبيق الأساسي (المستخدمين والصفحات العامة)
    path('', include('core.urls')),

    # 🛒 تطبيق المتجر (المنتجات والتصنيفات)
    path('store/', include('store.urls')),

    # 📦 تطبيق الطلبات والمدفوعات
    path('orders/', include('orders.urls')),
]


# ==============================
# ⚙️ إعدادات الملفات الثابتة والإعلامية أثناء التطوير
# ==============================
if settings.DEBUG:
    # عرض الملفات المرفوعة من المستخدمين (media)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # عرض الملفات الثابتة (static)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
