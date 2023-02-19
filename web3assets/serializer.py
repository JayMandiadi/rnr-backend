from rest_framework import serializers
from .models import AssetInstance, User


class AssetInstanceSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    asset = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = AssetInstance
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "password",
            "last_login",
            "is_superuser",
            "is_staff",
            "is_active",
            "groups",
            "user_permissions",
            "date_joined",
        )
