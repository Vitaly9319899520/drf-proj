from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions



urlpatterns = [
    path('admin/', admin.site.urls),
    path('materials/', include('materials.urls', namespace='materials')),
    path('users/', include('users.urls', namespace='users')),
]
