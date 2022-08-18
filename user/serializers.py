from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueTogetherValidator

from user.models import CustomUser


class CustomUserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=30)
    city = serializers.CharField(max_length=30)
    avatar = serializers.ImageField()
    password = serializers.CharField()

    def validate_email(self, email):
        emails = CustomUser.objects.all().values_list('email', flat=True)
        if email in emails:
            raise ValidationError("User with this email already exists!")

        return email

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)

    class Meta:
        model = CustomUser
        validators = [
            UniqueTogetherValidator(
                queryset=CustomUser.objects.all(),
                fields=['email']
            )
        ]
