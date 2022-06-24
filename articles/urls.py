from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('blog/', views.blog, name='blog'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('contacts/', views.Contacts.as_view(), name='contacts'),
    path('calc/', views.Calc.as_view(), name='calc')
]
