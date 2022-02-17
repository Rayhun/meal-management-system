# django import
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# local import
from meal.models.abstract.abstract import AbstractBaseModel


class Profile(AbstractBaseModel):
    """
    Profile model.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    profile_pic = models.ImageField(
        upload_to='profile_pic', blank=True
    )

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
