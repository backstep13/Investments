from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name="profile"),
    path('add/', views.add_view, name="add"),
    path('back/<int:pk>/', views.back_view, name="back"),
    path('del/<int:pk>/', views.del_investment, name="del"),
    path('account/<int:pk>/', views.AccountUpdateView.as_view(), name="account"),
]
