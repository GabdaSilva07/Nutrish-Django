from django import urls
from django.urls import path
from .views import PostInfoList, PostInfoDetail

app_name = 'User_info'

urlpatterns = [
    path('', PostInfoList.as_view(), name='post_list'),
    path('<int:pk>/', PostInfoDetail.as_view(), name='post_detail')
]



