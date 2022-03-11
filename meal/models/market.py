from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

from meal.models.abstract import AbstractBaseModel

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class ToDo(AbstractBaseModel):
    """
    Todo model.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Item(AbstractBaseModel):
    """
    Item model.
    """
    name = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class NeedItem(models.Model):
    """
    NeedItem model.
    """
    name = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.item.name


class Market(AbstractBaseModel):
    """
    Market model.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    item = models.ForeignKey(
        Item, on_delete=models.SET_NULL, null=True
    )
    total_cost = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )
    date = models.DateField(blank=True)

    def __str__(self):
        return self.name
