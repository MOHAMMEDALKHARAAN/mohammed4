from django.shortcuts import render

def home(request):
    """عرض الصفحة الرئيسية لمتجر أدوات السلامة"""
    return render(request, 'home.html')
