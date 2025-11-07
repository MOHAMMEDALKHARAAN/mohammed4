from django.shortcuts import render

def store_home(request):
    """عرض صفحة المنتجات الرئيسية (Store Page)"""
    # منتجات تجريبية (قابلة للاستبدال لاحقًا من قاعدة البيانات)
    products = [
        {"name": "خوذة أمان صناعية", "price": "75", "image": "helmet.png"},
        {"name": "قفازات مقاومة للحرارة", "price": "45", "image": "gloves.png"},
        {"name": "نظارات واقية شفافة", "price": "35", "image": "goggles.png"},
        {"name": "حذاء سلامة فولاذي", "price": "120", "image": "boots.png"},
        {"name": "طفاية حريق بودرة 6كجم", "price": "150", "image": "extinguisher.png"},
    ]
    return render(request, 'store.html', {'products': products})
