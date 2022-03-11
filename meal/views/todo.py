from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin

from meal.models.market import ToDo


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
