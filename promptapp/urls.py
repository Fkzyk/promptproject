from django.urls import path
from . import views

app_name = 'promptapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('categories/<str:category_name>/', views.category_list, name='category_list'),
    path('privacypolicy/', views.PrivacypolicyView.as_view(), name='privacypolicy'),
    path('mypage/', views.MyPageView.as_view(), name='mypage'),
]
