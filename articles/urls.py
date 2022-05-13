from django.urls import path
from . import views


app_name = 'articles'

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:article_id>/', views.detail, name='detail'),
]
