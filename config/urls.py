from django.contrib import admin
from django.urls import path, include

from config import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("on_learning.urls", namespace="on_learning")),
    path("users/", include("users.urls", namespace="users")),
    path("api-auth/", include("rest_framework.urls")),
]
