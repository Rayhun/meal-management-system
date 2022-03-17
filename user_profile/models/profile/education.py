# django import
from django.db import models

# local import
from meal.models.abstract.abstract import AbstractBaseModel
from user_profile.models.profile.profile import Profile


class University(models.Model):
    """
    University model.
    """
    name = models.CharField(max_length=255, blank=True)

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
    degree = models.CharField(max_length=255, null=True)
    subject = models.CharField(max_length=255, null=True)
    result = models.CharField(max_length=255, blank=True)
    university = models.ForeignKey(
        University, on_delete=models.SET_NULL, blank=True, null=True
    )
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.profile.user.username


class Skill(AbstractBaseModel):
    """
    Skill model.
    """

    SKILL = (
        ('1', 'Beginner'),
        ('2', 'Intermediate'),  
        ('3', 'Advanced'),
    )

    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, blank=True, related_name="skill"
    )
    name = models.CharField(max_length=255, blank=True)
    type = models.CharField(
        choices=SKILL, null=True, default="3", max_length=1
    )

    def __str__(self):
        return self.profile.user.username
