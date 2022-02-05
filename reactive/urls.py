from django.urls import path, include
from django.contrib import admin
from button import views


urlpatterns = [
    path("unicorn/", include("django_unicorn.urls")),
    path("", views.index, name="index"),
    path('profile/', include('button.urls')),
    path('register/', views.register, name="register"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('api/investor/<int:pk>/', views.APIInvestor.as_view()),
    path('api/investments/<int:pk>/', views.api_investment)
]