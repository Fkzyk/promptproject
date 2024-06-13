from django.urls import path
from . import views

app_name = 'promptapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('categories/<str:category_name>/', views.category_list, name='category_list'),
    path('privacypolicy/', views.PrivacypolicyView.as_view(), name='privacypolicy'),
    path('mypage/', views.MyPageView.as_view(), name='mypage'),
    path('search/', views.search, name='search'),
    path('category/<str:category_name>/', views.category_search, name='category_search'),
    path('prompt/<int:pk>/', views.PromptDetailView.as_view(), name='prompt_detail'),
    path('search/', views.search, name='search'),
]