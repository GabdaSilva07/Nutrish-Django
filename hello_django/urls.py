from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include


def home(request):
    return JsonResponse({"hello": "world!"})


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include('UserAPI.urls')),
    path("", include('accounts.urls')),
]
