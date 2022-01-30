from django.urls import path, include
from django.contrib import admin
from button import views


urlpatterns = [
    path("", views.index),
    path("button/", include("django_unicorn.urls")),
    path('accounts/profile/add/', views.AddCreateView.as_view(), name="add"),
    path('accounts/profile/account/', views.AccountCreateView.as_view(), name="account"),
    path('accounts/profile/', views.profile, name="profile"),
    path('accounts/register/', views.register, name="register"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('api/investor/<int:pk>/', views.api_investor),
    path('api/investments/<int:pk>/', views.api_investment)
]
