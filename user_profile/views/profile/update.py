from django.views.generic import UpdateView
from django.contrib.auth.mixins import (
    LoginRequiredMixin, UserPassesTestMixin
)
from user_profile.models.profile import Profile
from user_profile.forms.profile import ProfileForm


class ProfileUpdateView(
    LoginRequiredMixin, UserPassesTestMixin, UpdateView
):
    """
    Profile Update view.
    """
    model = Profile
    form_class = ProfileForm
    template_name = 'profile/profile_update.html'
    permission = 'meal.add_profile'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser
