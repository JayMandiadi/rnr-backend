from rest_framework import status
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from web3assets.models import AssetInstance
from . import serializer

from django.conf import settings

User = settings.AUTH_USER_MODEL


class UserAssetsApi(ReadOnlyModelViewSet):
    http_method_names = ["get"]
    queryset = AssetInstance.objects.all()
    serializer_class = serializer.AssetInstanceSerializer
    permission_classes = (IsAuthenticated,)

    @action(methods=["GET"], detail=False)
    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.queryset, many=True)
        # serializer.is_valid(raise_exception=True)

        return Response(
            {
                "status": status.HTTP_200_OK,
                "message": "Assets retrieved.",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )
