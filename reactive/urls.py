from django.urls import path, include
from django.contrib import admin
from button import views


urlpatterns = [
    path("", views.index),
    path("button/", include("django_unicorn.urls")),
    path('accounts/profile/', views.profile, name="profile"),
    path('accounts/register/', views.register, name="register"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls)
]
