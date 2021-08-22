from rest_framework import serializers
from .models import Info

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ('id', 'author', 'diet', 'intolerance', 'favourite1', 'favourite2', 'favourite3')