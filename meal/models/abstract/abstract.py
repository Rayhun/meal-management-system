from django.db import models


class AbstractBaseModel(models.Model):
    """
    Abstract base model for all models.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)

    class Meta:
        abstract = True
