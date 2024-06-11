from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from .models import Category, Prompt

class IndexView(TemplateView):
    template_name = 'index.html'

def category_list(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    items = Prompt.objects.filter(category=category)
    
    template_name = f'{category_name.lower()}-list.html'
    return render(request, template_name, {'items': items})

class PrivacypolicyView(TemplateView):
    template_name = "privacypolicy.html"

class MyPageView(TemplateView):
    template_name = 'mypage.html'