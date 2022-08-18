from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from advertisement.models import Advertisement
from user.models import CustomUser


class AdvertisementSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    user = serializers.PrimaryKeyRelatedField(queryset= CustomUser.objects.all())
    description = serializers.CharField()
    head_image = serializers.ImageField()




