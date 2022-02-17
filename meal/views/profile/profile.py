from django.views.generic import TemplateView
from django.contrib.auth.mixins import (
    LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin,
)
from meal.models.profile import Profile


class ProfileView(
    LoginRequiredMixin, UserPassesTestMixin,
    TemplateView
):
    """
    Profile view.
    """
    template_name = 'profile/profile.html'

    def test_func(self):
        return self.request.user.is_active

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(user=self.request.user)
        return context
