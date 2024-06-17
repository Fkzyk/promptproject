import os
import random
from django.conf import settings

def get_random_photos():
    categories = ['creative', 'study', 'business', 'lifestyle', 'technology', 'travel']
    selected_photos = {}

    for category in categories:
        category_path = os.path.join(settings.BASE_DIR, 'static', 'img', category)
        if os.path.exists(category_path):
            photos = os.listdir(category_path)
            if photos:
                selected_photos[category] = os.path.join('img', category, random.choice(photos))

    return selected_photos
