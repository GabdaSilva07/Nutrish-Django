from rest_framework import generics, permissions
from .models import Info
from .serializers import InfoSerializer
from rest_framework.permissions import BasePermission, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly


class PostInfoWritePermissions(BasePermission):
    message = "Editing is restricted to the author only."

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user


class PostInfoList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Info.objects.all()
    serializer_class = InfoSerializer




class PostInfoDetail(generics.RetrieveUpdateDestroyAPIView, PostInfoWritePermissions):
    permission_classes = [PostInfoWritePermissions]
    queryset = Info.objects.all()
    serializer_class = InfoSerializer