from django.shortcuts import redirect
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import (
    LoginRequiredMixin, UserPassesTestMixin
)
from user_profile.models.profile import Profile, Education
from user_profile.forms.profile import ProfileForm, EducationFormSet


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

    def get_context_data(self, **kwargs):
        if self.request.POST:
            kwargs['formset'] = EducationFormSet(
                self.request.POST, queryset=Education.objects.none(),
                prefix='formset'
            )
        else:
            kwargs['formset'] = EducationFormSet(
                queryset=Education.objects.none(),
                prefix='formset'
            )
        return super().get_context_data(**kwargs)
    
    def post(self, request, *args, **kwargs):
        # get object
        self.object = self.get_object()
        # get form
        form = self.get_form()
        formset = EducationFormSet(
            self.request.POST,
            queryset=Education.objects.none(),
            prefix='formset'
        )
        if form.is_valid() and formset.is_valid():
            formsets = formset.save(commit=False)
            # formset delete
            for forms in formset.deleted_objects:
                forms.delete()
            # formset save
            for forms in formsets:
                forms.profile = self.object
                forms.save()
            return self.form_valid(form)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        url = reverse_lazy('user_profile:profile_view')
        messages.success(
            self.request, 'community based water supply created successfully!')
        return url
    

    def test_func(self):
        return self.request.user.is_superuser
