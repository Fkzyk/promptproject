from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView
from .models import Category, Prompt

category_map = {
    'creative': 'クリエイティブ',
    'study': '学習',
    'business': 'ビジネス',
    'lifestyle': 'ライフスタイル',
    'technology': 'テクノロジー',
    'travel': '旅行'
}

class IndexView(TemplateView):
    template_name = 'index.html'

def category_list(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    items = Prompt.objects.filter(category=category)
    
    template_name = f'{category_name.lower()}-list.html'
    return render(request, template_name, {'items': items})

def category_search(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    prompts = Prompt.objects.filter(category=category)
    categories = Category.objects.all()

    return render(request, 'mypage.html', {
        'prompts': prompts,
        'categories': categories,
        'selected_category': category_name,  # 選択されたカテゴリ名を追加
    })

class PrivacypolicyView(TemplateView):
    template_name = "privacypolicy.html"

class MyPageView(TemplateView):
    template_name = 'mypage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['prompts'] = Prompt.objects.all()
        context['category_map'] = category_map
        return context

def search(request):
    query = request.GET.get('q')
    category_name = request.GET.get('category')
    prompts = Prompt.objects.all()

    if query:
        prompts = prompts.filter(description__icontains=query) | prompts.filter(content__icontains=query)

    if category_name:
        category = get_object_or_404(Category, name=category_name)
        prompts = prompts.filter(category=category)

    categories = Category.objects.all()
    return render(request, 'search_results.html', {'prompts': prompts, 'categories': categories, 'category_map': category_map})

class PromptDetailView(DetailView):
    model = Prompt
    template_name = 'prompt_detail.html'
    context_object_name = 'prompt'