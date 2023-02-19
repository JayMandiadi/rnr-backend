from rest_framework import status
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from web3assets.models import AssetInstance, User
from . import serializer


class UserAssetsApi(ReadOnlyModelViewSet):
    http_method_names = ["get"]
    queryset = AssetInstance.objects.all()
    serializer_class = serializer.AssetInstanceSerializer
    permission_classes = (IsAuthenticated,)

    @action(methods=["GET"], detail=False)
    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            self.queryset.filter(owner=request.user.id), many=True
        )
        # serializer.is_valid(raise_exception=True)

        return Response(
            {
                "status": status.HTTP_200_OK,
                "message": "Assets retrieved.",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )


class UserInfoApi(ReadOnlyModelViewSet):
    http_method_names = ["get"]
    queryset = User.objects
    serializer_class = serializer.UserSerializer
    permission_classes = (IsAuthenticated,)

    @action(methods=["GET"], detail=False)
    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.queryset.get(id=request.user.id))

        return Response(
            {
                "status": status.HTTP_200_OK,
                "message": "User details retrieved.",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )
