from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include



urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("api/", include('UserAPI.urls')),
    path("", include('accounts.urls')),
]
