from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import SimpleRouter

from button import views


router = SimpleRouter()
router.register(r'inv', views.APIInvestment, basename='investments')

urlpatterns = [
    path("unicorn/", include("django_unicorn.urls")),
    path('', include('articles.urls')),
    path('profile/', include('button.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls)
]
