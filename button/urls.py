from django.urls import path
from . import views


urlpatterns = [
    path('', views.Profile.as_view(), name="profile"),
    path('add/', views.AddView.as_view(), name="add"),
    path('back/<int:pk>/', views.BackView.as_view(), name="back"),
    path('del/<int:pk>/', views.DelView.as_view(), name="del"),
    path('account/<int:pk>/', views.AccountUpdateView.as_view(), name="account"),
]
