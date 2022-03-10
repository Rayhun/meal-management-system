# django import
from unittest import result
from django.db import models

# local import
from meal.models.abstract.abstract import AbstractBaseModel
from user_profile.models.profile.profile import Profile


class University(AbstractBaseModel):
    """
    University model.
    """
    name = models.CharField(max_length=255, blank=True, null=True)
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return self.name


class Education(AbstractBaseModel):
    """
    Education model.
    """
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, blank=True, null=True,
        related_name="education"
    )
    result = models.CharField(max_length=255, blank=True, null=True)
    university = models.ForeignKey(
        University, on_delete=models.SET_NULL, blank=True, null=True
    )
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user


class Skill(AbstractBaseModel):
    """
    Skill model.
    """
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, blank=True, null=True,
        related_name="skill"
    )
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user
