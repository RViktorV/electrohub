from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),  # Админ-панель
    path("", include("electronics_hub.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),  # Получение токена
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),  # Обновление токена

]
