from django.urls import path, include
from button import views


urlpatterns = [
    path("", views.index),
    path("button/", include("django_unicorn.urls"))
]
