from .models import User
from rest_framework import viewsets, permissions
from .serializer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permissions = [
        permissions.IsAuthenticated
    ]
    serializer_class = UserSerializer


    def get_queryset(self):
        return self.request.user.users.all()


    def get_permissions(self):
        if self.request.method == 'POST':
            return []
        return super().get_permissions()