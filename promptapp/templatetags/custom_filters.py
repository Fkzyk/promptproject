from django import template
import random

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

@register.filter
def random_photo(photos):
    if photos:
        return random.choice(photos)
    return None

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
