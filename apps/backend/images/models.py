import uuid

from django.contrib.postgres.fields import ArrayField, JSONField
from django.db import models
from app.models import Common


class ImageGroup(Common):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    processed = models.BooleanField(default=False)
    tags = JSONField(null=True)


class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    height = models.PositiveIntegerField(null=True)
    width = models.PositiveIntegerField(null=True)
    file = models.ImageField(null=True)
    external_url = models.URLField(null=True)
    permissions = ArrayField(models.PositiveIntegerField(), default=list)
    image_group = models.ForeignKey(
        "ImageGroup", related_name="images", on_delete=models.SET_NULL, null=True
    )



