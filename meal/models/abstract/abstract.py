from django.db import models
from django.conf import settings


class AbstractBaseModel(models.Model):
    """
    Abstract base model for all models.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    created_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        blank=True, null=True, related_name="%(app_label)s_%(class)s_createdby"
    )
    updated_at = models.DateTimeField(auto_now=True)
    updated_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        blank=True, null=True, related_name="%(app_label)s_%(class)s_updated"
    )
    delete_at = models.DateTimeField(blank=True, null=True)
    deleted_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        blank=True, null=True, related_name="%(app_label)s_%(class)s_deleted"
    )
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)

    class Meta:
        abstract = True
