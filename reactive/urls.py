import debug_toolbar
from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import SimpleRouter

from button import views


router = SimpleRouter()
router.register(r'inv', views.APIInvestment, basename='investments')

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path("unicorn/", include("django_unicorn.urls")),

    path("", views.Index.as_view(), name="index"),
    path('profile/', include('button.urls')),
    path('articles/', include('articles.urls')),
    path('register/', views.register, name="register"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
