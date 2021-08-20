from django.db import router
from django.urls import path
from .views import UserViewSet, mainPage
from rest_framework import routers
from django.conf.urls import include
from rest_framework.authtoken.views import obtain_auth_token
from .api import UserViewSet


router = routers.DefaultRouter()
router.register('users', UserViewSet, "users")

urlpatterns = [
    path("home/", mainPage),
    path("", include(router.urls)),
    # path("auth/", obtain_auth_token)
]
