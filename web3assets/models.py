# flake8: noqa

from django.db import models
from django.contrib.auth.models import AbstractUser

import uuid  # For unique asset instances


# Create your models here.
class User(AbstractUser):
    netWorth = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    realizedReturns = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    unrealizedReturns = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self) -> str:
        """String for representing the Model object (in Admin site etc.)"""
        return self.email


class Asset(models.Model):
    name = models.CharField(max_length=50, default="")

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class AssetInstance(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, help_text="Unique ID for this user asset"
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    exchange = models.CharField(max_length=99, default="")
    amount = models.DecimalField(max_digits=16, decimal_places=8, default=0)
    realizedPl = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    unrealizedPl = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    totalPl = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return "%s %s" % (self.asset.name, self.owner.email)
