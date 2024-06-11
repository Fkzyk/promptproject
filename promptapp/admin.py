from django.contrib import admin

from .models import Account, MyFavo, Category, Prompt

admin.site.register(Account)
admin.site.register(MyFavo)
admin.site.register(Category)
admin.site.register(Prompt)
