from django import forms
from meal.models.profile import Profile


class ProfileForm(forms.ModelForm):
    """
    Profile form.
    """
    class Meta:
        model = Profile
        fields = ['dob', 'mobile', 'address', 'profile_pic']
