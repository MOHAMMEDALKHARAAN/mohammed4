from django.shortcuts import render

def home(request):
    """عرض الصفحة الرئيسية"""
    return render(request, 'base.html')
