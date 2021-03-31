import uuid
from django.db import models


class Common(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True

    def export_to_dict(self, exclude=[]):
        return dict(
            (key, val) for key, val in sorted(vars(self).items()) if not key.startswith("_") and key not in exclude
        )
