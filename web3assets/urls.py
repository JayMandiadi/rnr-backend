# flake8: noqa
from django.urls import path
from .views import UserAssetsApi

urlpatterns = [path("me/", UserAssetsApi.as_view({"get": "list"}), name="user_assets")]
