from rest_framework import viewsets, permissions
from .serializer import UserInfoSerializer
from .models import UserInfo

# Lead Viewset


class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserInfoSerializer

    # def get_queryset(self):
    #     return self.request.user.UserInfo.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)