from django.urls import path
from .views import CustomUserCreate, BlacklistTokenUpdateView, UserInfo


app_name = "users"

urlpatterns = [
    path("userinfo/", UserInfo.as_view()),
    path("register/", CustomUserCreate.as_view(), name="create_user"),
    path("logout/blacklist/", BlacklistTokenUpdateView.as_view(), name="blacklist")
]
