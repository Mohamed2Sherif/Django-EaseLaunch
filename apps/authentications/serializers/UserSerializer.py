from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "name",
            "email",
            "avatar",
            "is_superuser",
            "date_joined",
            "last_login",
        ]


class UserSerializerPublic(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    avatar = serializers.ImageField()


class UserSerializerPrivate(UserSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "name", "email", "avatar"]


class UserStatusAuth(serializers.Serializer):
    status = serializers.BooleanField(required=False, read_only=True)
