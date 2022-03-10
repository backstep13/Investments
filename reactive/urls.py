from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import SimpleRouter

from button import views


router = SimpleRouter()
router.register(r'inv', views.APIInvestment, basename='investments')

urlpatterns = [
    path("unicorn/", include("django_unicorn.urls")),
    path("", views.index, name="index"),
    path('profile/', include('button.urls')),
    path('register/', views.register, name="register"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
