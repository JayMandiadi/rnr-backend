from rest_framework import serializers
from .models import AssetInstance


class AssetInstanceSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    asset = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = AssetInstance
        fields = "__all__"
