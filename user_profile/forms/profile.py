from django import forms
from user_profile.models.profile import Profile


class ProfileForm(forms.ModelForm):
    """
    Profile form.
    """
    class Meta:
        model = Profile
        fields = ['dob', 'mobile', 'address', 'profile_pic']

        widgets = {
            'dob': forms.TextInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                    'type': 'date',
                }
            ),
            'mobile': forms.NumberInput(
                attrs={
                    'type': 'number',
                    'class': 'form-control'
                }
            ),
            'address': forms.Textarea(
                attrs={
                    'rows': '3',
                    'class': 'form-control'
                }
            ),
        }
