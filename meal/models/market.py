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
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    description = models.TextField(blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    @property
    def progres(self):
        """
        Return the progress of the todo in percent.
        """
        need_item = NeedItem.objects.filter(
            todo=self, todo__is_completed=False
        ).count()
        print(need_item, "*" * 50)
        todo = ToDo.objects.filter(
            user=self.user, is_completed=False,
            start_date__lte=self.start_date, end_date__gte=self.end_date
        )
        a = todo.count()
        return 0

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
    todo = models.ForeignKey(
        ToDo, on_delete=models.SET_NULL, null=True, related_name='need_items'
    )
    name = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.todo.name} - {self.name}"


class Market(AbstractBaseModel):
    """
    Market model.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    item = models.ForeignKey(
        Item, on_delete=models.SET_NULL, null=True
    )
    total_cost = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )
    date = models.DateField(blank=True)

    def __str__(self):
        return self.name
