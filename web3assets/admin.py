from django.contrib import admin

# Register your models here.
from .models import User, Asset, AssetInstance

# from django.contrib.auth.admin import UserAdmin


# class MainAdmin(UserAdmin):
#     pass


admin.site.register(User)
admin.site.register(Asset)
admin.site.register(AssetInstance)
