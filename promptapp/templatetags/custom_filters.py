from django import template

register = template.Library()

@register.filter
def translate_category(value):
    translations = {
        'creative': 'クリエイティブ',
        'study': '学習',
        'business': 'ビジネス',
        'lifestyle': 'ライフスタイル',
        'technology': 'テクノロジー',
        'travel': '旅行'
    }
    return translations.get(value, value)

