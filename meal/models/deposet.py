from django.db import models
from django.contrib.auth.models import User

from meal.models.abstract import AbstractBaseModel


class Deposet(AbstractBaseModel):
    uset = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True,
        related_name="user_deposet"
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.amount}"
