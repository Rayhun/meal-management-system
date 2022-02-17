from django.views.generic import CreateView
from django.contrib.auth.mixins import (
    LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin,
)
from meal.models.profile import Profile
from meal.forms.profile import ProfileForm


class ProfileCreateView(
    LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin,
    CreateView
):
    """
    Profile create view.
    """
    model = Profile
    form_class = ProfileForm
    template_name = 'profile/profile_create.html'
    permission = 'meal.add_profile'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser