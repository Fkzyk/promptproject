from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Account, MyFavo, Category, Prompt

# 各モデルに対するResourceクラスを作成
class AccountResource(resources.ModelResource):
    class Meta:
        model = Account

class MyFavoResource(resources.ModelResource):
    class Meta:
        model = MyFavo

class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category

class PromptResource(resources.ModelResource):
    class Meta:
        model = Prompt
        fields = ('id', 'title', 'description', 'content', 'category_id', 'created_at', 'updated_at')
        export_order = ('id', 'title', 'description', 'content', 'category_id', 'created_at', 'updated_at')

# 各モデルに対するAdminクラスを作成
class AccountAdmin(ImportExportModelAdmin):
    resource_class = AccountResource

class MyFavoAdmin(ImportExportModelAdmin):
    resource_class = MyFavoResource

class CategoryAdmin(ImportExportModelAdmin):
    resource_class = CategoryResource

class PromptAdmin(ImportExportModelAdmin):
    resource_class = PromptResource

# 管理サイトにモデルを登録
admin.site.register(Account, AccountAdmin)
admin.site.register(MyFavo, MyFavoAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Prompt, PromptAdmin)