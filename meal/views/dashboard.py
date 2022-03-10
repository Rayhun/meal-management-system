from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class DashboardView(
    LoginRequiredMixin, UserPassesTestMixin, TemplateView
):
    template_name = 'dashboard.html'

    def test_func(self):
        return self.request.user.is_active
