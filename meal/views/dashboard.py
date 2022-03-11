from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from meal.models.market import ToDo


class DashboardView(
    LoginRequiredMixin, UserPassesTestMixin, TemplateView
):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo_list'] = ToDo.objects.filter(
            user=self.request.user
        ).order_by('-created_at')
        return context

    def test_func(self):
        return self.request.user.is_active
