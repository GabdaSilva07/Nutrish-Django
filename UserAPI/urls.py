from django.db import router
from django.urls import path
from .views import  mainPage
from .api import UserInfoViewSet
from rest_framework import routers
from django.conf.urls import include
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()

router.register('users', UserInfoViewSet)

router.register('users', UserViewSet)


urlpatterns = [
    path("home/", mainPage),
    path("", include(router.urls)),
    path("auth/", obtain_auth_token)
]
