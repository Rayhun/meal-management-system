from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
)

from meal.models.market import ToDo
from meal.forms import ToDoForm


class TodoListView(
    LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, ListView
):
    """ View for the todo list """
    model = ToDo
    template_name = 'meal/todo/list.html'
    context_object_name = 'todos'
    permission_required = 'meal.view_todo'

    def test_func(self):
        return self.request.user.has_perm(self.permission_required)


class TodoCreateView(
    LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, CreateView
):
    """ View for creating a new todo """
    model = ToDo
    template_name = 'meal/todo/create.html'
    permission_required = 'meal.add_todo'
    form_class = ToDoForm

    def test_func(self):
        return self.request.user.has_perm(self.permission_required)
