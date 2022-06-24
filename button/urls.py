from django.urls import path
from . import views


app_name = 'button'

urlpatterns = [
    path('', views.Profile.as_view(), name="profile"),
    path('account/<int:pk>/', views.AccountUpdateView.as_view(), name="account"),
    path('add/', views.AddView.as_view(), name="add"),
    path('back/<int:pk>/', views.BackView.as_view(), name="back"),
    path('del/<int:pk>/', views.DelView.as_view(), name="del")  # may be not to use
]
